from django.contrib import admin
from .models import *


class HotelAdmin(admin.ModelAdmin):
    filter_horizontal= ('Facilitys',)

admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(owner)
admin.site.register(Rooms)
admin.site.register(Facility)
admin.site.register(Booking)
