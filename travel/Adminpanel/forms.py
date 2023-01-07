from Adminpanel.models import Chauffeurs, Car, Agent, Gare,Ticket
from django import forms
from django.contrib.auth.models import User
from django.conf import settings


class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chauffeurs
        fields = "__all__"
        exclude = ('user',)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"
        exclude = ('user',)


class GareForm(forms.ModelForm):
    class Meta:
        model = Gare
        fields = "__all__"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')



class TicketReservationForm(forms.Form):
    
    #class Meta:
     #   model = Ticket
     #   fields = '__all__'
 
    passenger_name = forms.CharField(max_length=255)
    ticket_number = forms.CharField(max_length=255)
    destination = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    
    def clean(self):
        cleaned_data = super().clean()
        # Vérifiez que le prix est supérieur à zéro
        if cleaned_data['price'] <= 0:
            raise forms.ValidationError("Le prix doit être supérieur à zéro.")
        # Vérifiez que le nom du passager n'est pas vide
        if not cleaned_data['passenger_name']:
            raise forms.ValidationError("Le nom du passager est requis.")
        # Vérifiez que la destination n'est pas vide
        if not cleaned_data['destination']:
            raise forms.ValidationError("La destination est requise.")