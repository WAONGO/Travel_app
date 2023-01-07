from django.shortcuts import render, redirect
from Adminpanel.models import Ticket
from Adminpanel.forms import TicketReservationForm




def ticket_reservation(request):
    if request.method == 'POST':
        # Traitez la soumission de formulaire
        form = TicketReservationForm(request.POST)
        if form.is_valid():
            # Enregistrez le billet de voyage dans la base de données
            ticket = Ticket(**form.cleaned_data)
            ticket.save()
            
            # Redirigez l'utilisateur vers une page de confirmation de réservation
            return redirect('Booking:reservation_confirmation')
    else:
        # Affichez le formulaire de réservation de billets de voyage
        form = TicketReservationForm()
    return render(request, 'ticket_reservation.html', {'form':form})

def reservation_confirmation(request):
    if request.method == 'POST':
        # Récupérez les données du formulaire soumis par l'utilisateur
        passenger_name = request.POST['passenger_name']
        ticket_number = request.POST['ticket_number']
        destination = request.POST['destination']
        price = request.POST['price']

        # Créez un dictionnaire avec les détails de la réservation de l'utilisateur
        reservation_details = {
            'passenger_name': passenger_name,
            'ticket_number': ticket_number,
            'destination': destination,
            'price': price,
        }

        return render(request, 'reservation_confirmation.html', {'reservation_details': reservation_details})
    else:
        # Affichez une erreur si le formulaire n'a pas été soumis
        return render(request, 'error.html', {'message': 'Invalid request: the form was not submitted'})
