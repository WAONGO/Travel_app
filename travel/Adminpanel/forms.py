from Adminpanel.models import Chauffeurs, Car, Agent, Gare
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
