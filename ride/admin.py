from django.contrib import admin
from ride.models import*
# Register your models here.

# admin.site.register(User_pick_form)
class ItemAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Rider_Trip , ItemAdmin)



class IAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('select_truck_type','pick_point','drop_point' , 'distance' ,'total_price')
    # readonly_fields=('basefare','basekm',)
admin.site.register(User_pick_form , IAdmin)