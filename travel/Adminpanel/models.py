from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

# le modèle chauffeur


class Chauffeurs (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    permis = models.CharField(max_length=50)
    carte_identité = models.IntegerField()
    telephone = models.IntegerField()
    localité = models.CharField(max_length=50)


def __str__(self):
    return self.nom
# le modele gare


class Gare (models.Model):
    code = models.IntegerField()
    nom = models.CharField(max_length=50)
    gerant = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    heure_ouverture = models.DateTimeField(auto_now_add=True)
    heure_fermeture = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


def __str__(self):
    return self.nom

# le model de car


class Car (models.Model):
    nom = models.CharField(max_length=50)
    place = models.IntegerField()
    conducteur = models.ForeignKey("Chauffeurs", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    numero = models.IntegerField()


def __str__(self):
    return self.nom
# le model agent


class Agent (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    carte = models.CharField(max_length=50)
    telephone = models.IntegerField()
    idgare = models.ForeignKey("Gare",  on_delete=models.CASCADE)
    poste = models.CharField(max_length=50)


def __str__(self):
    return self.nom

# le model de ticket
class Ticket(models.Model):
    passenger_name = models.CharField(max_length=255)
    ticket_number = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    destination = models.CharField(max_length=255)
    

def __str__(self):
    return self.passenger_name
class Visiteur(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    ville = models.CharField(max_length=128)
    contact = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    
    
    

    def __str__(self):
        return self.nom 
    

    
    

