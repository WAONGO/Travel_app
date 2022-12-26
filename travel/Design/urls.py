from django.urls import path
from Design import views

app_name = 'Design'

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('recover/', views.recover, name='recover'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    

]
