from django.urls import path
from .views import chauffeur

app_name = 'Adminpanel'
urlpatterns = [
    path('', chauffeur.home, name='Adminpanel'),
    path('chauffeurs', chauffeur.chauffeur_list, name='chauffeur_list'),

    path('chauffeur-ajout', chauffeur.addchauffeur, name="add_chauffeur"),
    path('modifier-chauffeur/<int:pk>',
         chauffeur.updatechauffeur, name="modify_chauffeur"),
    path('delete-chauffeur/<int:pk>',
         chauffeur.DeleteChauffeur.as_view(), name="delete_chauffeur"),
]
