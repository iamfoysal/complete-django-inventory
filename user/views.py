from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserForm, UserRegisterFrom


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password= password)

        if user is not None:
            login (request, user)
            messages.success(request, "login successfully complete!!")
            return redirect('index')
        else:
            messages.error(request, "Password or User name is Wrong! Please try Again")
    return render(request, 'user/login.html')



def register(request):
    form = UserRegisterFrom ()
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created.")
            return redirect("signin")
    return render(request, 'user/register.html',{'form':form})



def signout(request):
    logout(request)
    messages.success(request, "logout Successfully Complete.")
    return redirect("signin")
