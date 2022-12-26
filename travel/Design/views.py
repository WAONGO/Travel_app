from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index2.html')


def service(request):
    return render(request, 'services.html')


def recover(request):
    return render(request, 'recover.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register_2.html')
