from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages

from Adminpanel.forms import ChauffeurForm, UserForm
from travel import settings

from Adminpanel.models import Chauffeurs
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import Group


# @login_required
def chauffeur_list(request):
    chauffeurs = Chauffeurs.objects.all().order_by("-id")
    context = {
        'p_title': "Les chauffeurs",
        'chauffeurs': chauffeurs
    }
    return render(request, 'chauffeurs/chauffeur_list.html', context)

# @login_required


def addchauffeur(request):
    form = ChauffeurForm
    userform = UserForm()
    default_password = '123456789'

    if request.method == 'POST':
        form = ChauffeurForm(request.POST)

        if form.is_valid():
            chauffeur = form.save(commit=False)
            chauffeur.statut = True if int(
                request.POST.get('status')) == 1 else False

            # Creation en arriere plan d'un compte utilisateur pour le partenaire nouvellment ajoute
            _user = userform.save(commit=False)
            _user.username = request.POST.get('nom')
            _user.password = make_password(default_password)
            _user.save()
            chauffeur.user = _user

            # fin creation de compte user

         # ajout du user au group PARTENAIRES
            chauffeur.save()

            user_group = Group.objects.get(name='Chauffeur')
            _user.groups.add(user_group)

            messages.success(request, settings.SUCCESS_MESSAGE)
            return redirect('Adminpanel:chauffeur_list')

        else:
            print('errors')
            form = ChauffeurForm

    context = {
        'p_title': "Ajouter un chauffeur",
        'form': form
    }
    return render(request, 'chauffeurs/chauffeur_addform.html', context)


# @login_required
def updatechauffeur(request, pk):
    chauffeurs = Chauffeurs.objects.get(pk=pk)

    form = ChauffeurForm(instance=chauffeur)

    if request.method == 'POST':
        form = ChauffeurForm(request.POST, instance=chauffeur)
        if form.is_valid():
            chauffeur = form.save(commit=False)
            # partenaire.statut = True if int(
            #  request.POST.get('etat')) == 1 else False
            chauffeur.save()

            messages.success(request, settings.SUCCESS_MESSAGE)
            return redirect('Adminpanel:chauffeur_list')
        else:
            form = ChauffeurForm()

    context = {
        'p_title': "Modifier chauffeur",
        'form': form,
        'chauffeur': chauffeur,
    }
    return render(request, 'chauffeurs/chauffeur_updateform.html', context)


class DeleteChauffeur(DeleteView):
    model = Chauffeurs

    def delete(self, request, *args, **kwargs):
        try:
            my_return = super().delete(request, *args, **kwargs)
            messages.success(self.request, settings.DELETE_MESSAGE)
        except IntegrityError:
            messages.error(self.request, settings.FAILURE_MESSAGE)
            my_return = redirect(
                'Adminpanel:modify_chauffeur', pk=self.get_object().pk)
        return my_return

    def get_success_url(self) -> str:
        return reverse_lazy('Adminpanel:chauffeur_list')
