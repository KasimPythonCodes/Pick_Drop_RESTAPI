from django.contrib import admin
from Userform.models import *
# Register your models here.
admin.site.register(Profile)


class IAdmin(admin.ModelAdmin):
    # # exclude=("headline ",)
    # list_display=('pick_point','drop_point' ,'distance_with_Bike',
    # 'total_price_Bike','distance_with_Champion','total_price_Champion',
    # 'distance_with_Ecovan','total_price_Ecovan','distance_with_Maruti',
    # 'total_price_Maruti','distance_with_Tata_ace_7FT','total_price_Tata_ace_7FT',
    # 'distance_with_Tata_ace_8FT','total_price_Tata_ace_8FT','distance_with_Blero_8FT','total_price_Blero_8FT',)
    # # readonly_fields=('basefare','basekm',)
    list_display=('pick_point','drop_point','distance')
admin.site.register(PICKFORM , IAdmin)