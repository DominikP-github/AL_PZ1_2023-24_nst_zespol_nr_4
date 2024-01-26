from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import SearchHistory,YourModel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import YourModelForm

def display_forms(request):
    forms_in_database = YourModel.objects.all()
    return render(request, 'special_page.html', {'forms_in_database': forms_in_database})

@login_required(login_url='login')
def form_page(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = YourModelForm()

    return render(request, 'form_page.html', {'form': form})

@login_required(login_url='login')
def success_page(request):
    return render(request, 'success_page.html')  # Create a success page template

@login_required(login_url='login')
def special_page(request):
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        all_forms = YourModel.objects.all()
        print("User is in 'SpecialGroup'")
        return render(request, 'special_page.html', {'all_forms': all_forms})
   
def delete_form(request, form_id):
    form = get_object_or_404(YourModel, id=form_id)

    if request.method == 'DELETE':
        form.delete()
        return JsonResponse({'message': 'Formularz został usunięty.'}, status=204)
    else:
        return JsonResponse({'error': 'Nieprawidłowa metoda żądania.'}, status=400)
       
@login_required(login_url='login')
def home_page(request):
    return render(request, 'home.html')

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

from django.shortcuts import render
from .models import Keyword, SearchHistory
from .forms import SearchForm

@login_required(login_url='login')
def home(request):
    # Sprawdzamy, czy użytkownik należy do grupy "SpecialGroup"
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        return redirect('special_page')  # Przekieruj na special_page.html

    user_search_history = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            keywords = Keyword.objects.values_list('word', 'opis_wyniku')
            found_descriptions = []

            for keyword in keywords:
                keyword_words = keyword[0].split()
                if all(word.lower() in sentence.lower() for word in keyword_words):
                    found_descriptions.append(keyword[1])

            description_with_html_line_breaks = "<br>".join(found_descriptions)

            # Zapisujemy wyszukiwanie w historii użytkownika
            if request.user.is_authenticated:
                user_history = SearchHistory.objects.create(
                    user=request.user,
                    sentence=sentence,
                    description=description_with_html_line_breaks
                )

            # Pobieramy historię wyszukiwań dla zalogowanego użytkownika
            user_search_history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')

            return render(request, 'home.html', {
                'sentence': sentence,
                'found_descriptions': found_descriptions,
                'user_search_history': user_search_history,
            })
    else:
        form = SearchForm()

    # Pobieramy historię wyszukiwań dla zalogowanego użytkownika (jeśli zalogowany)
    user_search_history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'home.html', {'form': form, 'user_search_history': user_search_history})

@login_required(login_url='login')
def special_page(request):
    # Sprawdzamy, czy użytkownik należy do grupy "SpecialGroup"
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        return render(request, 'special_page.html')  # Przekieruj na special_page.html
    else:
        return redirect('home') 



def search_history_detail(request, history_id):
    history_entry = get_object_or_404(SearchHistory, id=history_id)
    
    # Pobieramy wszystkie wpisy z historii wyszukiwań dla zalogowanego użytkownika (jeśli zalogowany)
    user_search_history = []
    if request.user.is_authenticated:
        user_search_history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    
    return render(request, 'search_history_detail.html', {'history_entry': history_entry, 'user_search_history': user_search_history})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def delete_history(request, history_id):
    history_entry = get_object_or_404(SearchHistory, id=history_id)
    history_entry.delete()
    return JsonResponse({'message': 'History entry deleted successfully'})
