from django.contrib import admin
import site
from Adminpanel.models import Chauffeurs, Car,  Gare, Agent

# Register your models here.
admin.site.site_header = 'ELITIS Express'
admin.site.index_title = 'Base de données'
admin.site.register(Chauffeurs)
admin.site.register(Car)
admin.site.register(Gare)
admin.site.register(Agent)
