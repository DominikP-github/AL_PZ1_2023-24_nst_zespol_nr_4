from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Historia,Fromularz,Slowa, Historia
from django.contrib.auth.models import Group
from .forms import YourModelForm,ChangeCredentialsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SearchForm

def display_forms(request):
    forms_in_database = Fromularz.objects.all()
    return render(request, 'special_page.html', {'forms_in_database': forms_in_database})

@login_required(login_url='login')
def form_page(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = YourModelForm()

    return render(request, 'form_page.html', {'form': form})

@login_required(login_url='login')
def success_page(request):
    return render(request, 'success_page.html')  

@login_required(login_url='login')
def special_page(request):
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        all_forms = Fromularz.objects.all()
        print("User is in 'SpecialGroup'")
        return render(request, 'special_page.html', {'all_forms': all_forms})
   
def delete_form(request, form_id):
    form = get_object_or_404(Fromularz, id=form_id)

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
            return HttpResponse ("Hasło lub Login jest nie poprawny!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Main(request):
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        return redirect('special_page')

    user_search_history = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            keywords = Slowa.objects.values_list('slowo', 'opis_wyniku')
            found_descriptions = []

            for keyword in keywords:
                keyword_words = keyword[0].split()
                if all(word.lower() in sentence.lower() for word in keyword_words):
                    found_descriptions.append(keyword[1])

            description_with_html_line_breaks = "<br>".join(found_descriptions)

            if request.user.is_authenticated:
                user_history = Historia.objects.create(
                    user=request.user,
                    sentence=sentence,
                    opis=description_with_html_line_breaks
                )

            user_search_history = Historia.objects.filter(user=request.user).order_by('-czas')

            return render(request, 'home.html', {
                'sentence': sentence,
                'found_descriptions': found_descriptions,
                'user_search_history': user_search_history,
            })
    else:
        form = SearchForm()

    user_search_history = Historia.objects.filter(user=request.user).order_by('-czas')

    return render(request, 'home.html', {'form': form, 'user_search_history': user_search_history})

@login_required(login_url='login')
def special_page(request):
    special_group = Group.objects.get(name='SpecialGroup')
    if special_group in request.user.groups.all():
        return render(request, 'special_page.html') 
    else:
        return redirect('home') 



def search_history_detail(request, history_id):
    history_entry = get_object_or_404(Historia, id=history_id)
    user_search_history = []
    if request.user.is_authenticated:
        user_search_history = Historia.objects.filter(user=request.user).order_by('-czas')
    
    return render(request, 'search_history_detail.html', {'history_entry': history_entry, 'user_search_history': user_search_history})

def delete_history(request, history_id):
    history_entry = get_object_or_404(Historia, id=history_id)
    history_entry.delete()
    return JsonResponse({'message': 'History entry deleted successfully'})


@login_required(login_url='login')
def change_credentials(request):
    if request.method == 'POST':
        form = ChangeCredentialsForm(request.POST)

        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            old_password = form.cleaned_data['old_password']

            if new_email:
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Email was successfully updated!')

            if new_password1 and new_password2 and old_password:
                password_form = PasswordChangeForm(request.user, {'old_password': old_password, 'new_password1': new_password1, 'new_password2': new_password2})
                if password_form.is_valid():
                    password_form.save()
                    messages.success(request, 'Password was successfully updated!')
                else:
                    messages.error(request, 'Password update failed. Please check the provided information.')

            if not new_email and not (new_password1 and new_password2 and old_password):
                messages.warning(request, 'No changes were made.')

            return redirect('home')
    else:
        form = ChangeCredentialsForm()

    return render(request, 'change_credentials.html', {'form': form})
