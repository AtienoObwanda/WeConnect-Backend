from multiprocessing.connection import Client
from django.contrib import admin

from accounts.models import Client, Owner

admin.site.register(Client)
admin.site.register(Owner)