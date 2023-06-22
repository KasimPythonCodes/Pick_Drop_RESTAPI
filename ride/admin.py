from django.contrib import admin
from ride.models import*
# Register your models here.


class BikeAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Bike_Trip , BikeAdmin)


class ChampionAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Champion_Trip , ChampionAdmin)


class EcoAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Ecovan_Trip , EcoAdmin)


# class BikeAdmin(admin.ModelAdmin):
#     # exclude=("headline ",)
#     list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
#     'price5_per_km','price6_per_km','extra1_distance'
#     ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
#     )
#     # readonly_fields=('basefare','basekm',)
# admin.site.register(Bike_Trip , BikeAdmin)


class MarutiAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Maruti_suzuki_super_carry_Trip , MarutiAdmin)


class TataAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Tata_ace_7FT_Trip , TataAdmin)

class BleroAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Blero_8FT_Trip , BleroAdmin)


class TataAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    list_display=('basefare','basekm','price1_per_km','price2_per_km','price3_per_km','price4_per_km',
    'price5_per_km','price6_per_km','extra1_distance'
    ,'extra2_distance','extra3_distance','extra4_distance','extra5_distance','extra6_distance'
    )
    # readonly_fields=('basefare','basekm',)
admin.site.register(Tata_ace_8FT_Trip , TataAdmin)


class TypeAdmin(admin.ModelAdmin):
    # exclude=("headline ",)
    # list_display=('id','vehicle_type1','vehicle_type2','vehicle_type3','vehicle_type4','vehicle_type5','vehicle_type6','vehicle_type7')
    # readonly_fields=('basefare','basekm',)
    list_display=('id', 'vehicle')
admin.site.register(Vehicle_type , TypeAdmin)

