from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from ride.views import*

from rest_framework import routers
router=routers.DefaultRouter()

# router.register('kasim' , index, basename='reg')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' ,include(router.urls)),
    path('api/auth/' ,include('rest_framework.urls')),
    # path('' , include('ride.urls'), name="kasim"),
    path('' , RegisterAPI.as_view() ,name='kasim')
]
