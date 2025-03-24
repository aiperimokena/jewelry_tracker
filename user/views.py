from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm

from django.contrib import messages
from django.shortcuts import render, redirect

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been registered!")
            return redirect('index')

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{error}')

    form = UserRegisterForm()
    return render(request, 'account/user_register.html',{'form': form} )

def user_login_view(request):

    if request.method == "POST":
       user_email = request.POST['email']
       user_password = request.POST['password']

       user = authenticate(request, username=user_email, password=user_password)

       if user:
            login(request, user)
            messages.success(request, "You have been loged in")
            return redirect('index')
       else:
            messages.error(request, "Wrong login or password")

    return render(request, 'account/user_login.html')

def user_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('index')