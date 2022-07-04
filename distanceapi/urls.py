from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from ride.views import*
from Userform.views import*

from Confirm_Booking.views import*
from rest_framework import routers

router=routers.DefaultRouter()

router.register('pick_and_drop_api' , RegisterAPI, basename='pick_and_drop_api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,include(router.urls ), name="pick_and_drop_api"),
    path('api/auth/' ,include('rest_framework.urls')),
    path('api' , include('ride.urls')),
    # path('' , RegisterAPI.as_view() ,name='pick_and_drop_api'),
    
    
    
    path('success' , success ,name='success'),
    
    path('check/pick_and_drop_api/api_view' , Check.as_view()  , name='check/pick_and_drop_api' ),
    path('check/point/Check_Champion' ,  Check_Champion.as_view() ,name='check/point/Check_Champion'),
    path('check/point/Check_bike' ,Check_bike.as_view() ,name='check/point/Check_bike'),
    path('check/pick_and_drop_api/Check_ecovan' , Check_ecovan.as_view()  , name='check/pick_and_drop_api/Check_ecovan' ),
    path('check/pick_and_drop_api/Check_Maruti_suzuki_super_carry_Trip' , Check_Maruti_suzuki_super_carry_Trip.as_view()  , name='check/pick_and_drop_api/Check_Maruti_suzuki_super_carry_Trip' ),
    path('check/pick_and_drop_api/Check_Tata_ace_7FT_Trip' , Check_Tata_ace_7FT_Trip.as_view()  , name='check/pick_and_drop_api/Check_Tata_ace_7FT_Trip' ),
    path('check/pick_and_drop_api//Check_Tata_ace_8FT_Trip' , Check_Tata_ace_8FT_Trip.as_view()  , name='check/pick_and_drop_api/Check_Tata_ace_8FT_Trip' ),
    path('check/pick_and_drop_api/Check_Blero_8FT_Trip' , Check_Blero_8FT_Trip.as_view()  , name='check/pick_and_drop_api/Check_Blero_8FT_Trip' ),
    
]


