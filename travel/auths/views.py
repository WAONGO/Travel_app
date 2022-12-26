from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from Adminpanel.models import Visiteur

from auths.forms import LoginForm
from auths.forms import  VisiteurForm
from Adminpanel.forms import UserForm
from django.contrib import messages
from travel import settings

def connexion(request,email=None,password=None):
    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['password']
        print('email', email)
        print('password', password)
        return render(request, "login.html")
    
def connectUser(request, username=None, password=None):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
            login(request, user)
            
            return redirect('Design:home')
    else:
        messages.info(request,"le nom d'utilisateur ou le mot de passe est incorrect?")
        return render(request, 'login.html')


def registerPage(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('auths:connectUser')
    else:
        form = UserCreationForm()
    return render(request, 'register_2.html', {'form': form})  
     

@login_required
def deconnexion(request):
    logout(request)
    return redirect('Design:index2')



