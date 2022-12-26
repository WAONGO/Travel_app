from django import forms
from django.contrib.auth.models import User
from Adminpanel.models import Visiteur


class LoginForm(forms.Form):
    email = forms.EmailField( widget=forms.EmailInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class VisiteurForm(forms.ModelForm):
    class Meta:
        model = Visiteur
        fields = "__all__"
        exclude = ('user',)
