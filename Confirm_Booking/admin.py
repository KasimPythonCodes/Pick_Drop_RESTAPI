from django.contrib import admin
from Confirm_Booking.models import*
# Register your models here.

class Confirm_Booking_Admin(admin.ModelAdmin):
    list_display=('vehicle' ,'pick_point' ,'drop_point' , 'price' , 'distance' ,'user')

admin.site.register(Confirm_Booking , Confirm_Booking_Admin)