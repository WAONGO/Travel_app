from django.urls import path
from . import views

app_name = "auths"


urlpatterns = [
    path('connexion/', views.connexion, name='connexion'),
    path('register/', views.register, name='register'),
]
