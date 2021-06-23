from django.contrib import admin
from .models import Client, ClientAddress,ClientService

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientAddress)
admin.site.register(ClientService)
