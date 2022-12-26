from django.urls import path
from . import views

app_name = "auths"


urlpatterns = [
    #path('connexion/', views.connexion, name='connexion'),
    path('connectUser/', views.connectUser, name='connectUser'),
    #path('register/', views.register, name='register'),
    path('registerPage/', views.registerPage, name='registerPage'),
    
]
