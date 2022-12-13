from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import Group
from Adminpanel.models import Visiteur

from auths.forms import LoginForm
from auths.forms import  VisiteurForm
from Adminpanel.forms import UserForm
from django.contrib import messages
from travel import settings


def connexion(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        next_url = request.POST.get('next')

        if form.is_valid():
            user = authenticate(request, email=email, password=password)

            if user:
                flag = check_password(user.password)

                if flag:
                    login(request, user=user)
                    messages.success(request, settings.SUCCESS_MESSAGE)
                    return redirect('login.html')

        else:
            form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    form = VisiteurForm()
    userform = UserForm()

    if request.method == 'POST':
        form = VisiteurForm(request.POST)
        if form.is_valid():
            visiteur = form.save()
            _user = userform.save()

            _user.save()
            visiteur.user = _user
            visiteur.save()

            user_group = Group.objects.get(name='Visiteur')
            _user.groups.add(user_group)

            messages.success(request, settings.SUCCESS_MESSAGE)
            return redirect('login.html')
        else:
            
            form = VisiteurForm()
    context = {
        'form': form
    }
    return render(request, 'index2.html', context)


@login_required
def deconnexion(request):
    logout(request)
    return redirect('Design:index2')
