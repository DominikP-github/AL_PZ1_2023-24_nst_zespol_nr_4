from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ZdanieForm
import spacy

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



# MojaAplikacja/views.py
from django.shortcuts import render
from django.conf import settings
from .forms import ZdanieForm
from .utils import wczytaj_klucze_z_pliku, wyszukaj_slowa_kluczowe
import os

def wyszukiwanie_slowa_kluczowego(request):
    message = None

    if request.method == 'POST':
        form = ZdanieForm(request.POST)
        if form.is_valid():
            zdanie_uzytkownika = form.cleaned_data['zdanie']

            # Pełna ścieżka do pliku z kluczami
            sciezka_pliku_z_kluczami = os.path.join(settings.BASE_DIR, 'app', 'Pliki', 'plik_z_kluczami.txt')

            klucze_slowa = wczytaj_klucze_z_pliku(sciezka_pliku_z_kluczami)

            if not klucze_slowa:
                message = "Brak kluczy słów w pliku."
            else:
                znalezione_slowa = wyszukaj_slowa_kluczowe(zdanie_uzytkownika, klucze_slowa)
                if znalezione_slowa:
                    message = "Znalezione słowa kluczowe: {}".format(", ".join(znalezione_slowa))
                else:
                    message = "Brak znalezionych słów kluczowych w zdaniu."

    else:
        form = ZdanieForm()

    return render(request, 'home.html', {'form': form, 'message': message})
