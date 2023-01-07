from django.urls import path
from . import views
app_name = 'Booking'
urlpatterns = [
    path('reservation/', views.ticket_reservation, name='ticket_reservation'),
    path('reservation/confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
]
