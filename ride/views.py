from Userform.models import*
from rest_framework import serializers
from django.shortcuts import render ,HttpResponse, redirect
from ride.models import*
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import*
from rest_framework.response import Response
from rest_framework import response
import datetime
from rest_framework.serializers import*
from ride.serializers import*
from django.views import View
from ride.forms import*
import geopy
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from geopy import*
from ride.pricechange import*
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import exceptions
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView

import requests
def h(request):
   
   return render(request , 'index.html')


# UserSerializer

class RegisterAPI(ModelViewSet):
    serializer_class = UserSerializerForm
    def get_queryset(self):
        post_data=PICKFORM.objects.all()
        return post_data
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        for p in Bike_Trip.objects.all():
            print("Bike_Trip")
        for C in Champion_Trip.objects.all():
            print(C.price1_per_km,"Champion")
        for E in Ecovan_Trip.objects.all():
            print(E.price1_per_km,"Ecovan")
        for M in Maruti_suzuki_super_carry_Trip.objects.all():
            print(M.price1_per_km,"Maruti")
        for T in Tata_ace_7FT_Trip.objects.all():
            print(T.price1_per_km,"Tata_ace_7FT_Trip")
        for TT in Tata_ace_8FT_Trip.objects.all():
            print(TT.price1_per_km,"Tata_ace_8FT")
        for B in Blero_8FT_Trip.objects.all():
            print(B.price1_per_km,"Blero_8FT_Trip")
        for K in Vehicle_type.objects.all():
            print(K.vehicle_type1,"Vehcle")
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        serializer.is_valid(raise_exception=True)
        geolocator = Nominatim(user_agent="kasim",timeout=10)
        user = serializer.save()    b
        n=user.pick_point
        n1=user.drop_point
        location1 = geolocator.geocode(n) 
        location2 = geolocator.geocode(n1)
        u1=user.pick_point=location1 
        u2=user.drop_point=location2 
        if u1 and u2:
            l1,l2=u1.latitude, u1.longitude
            l3,l4=u2.latitude, u2.longitude
            k = (l1, l2)
            de= (l3,l4)
            dis=great_circle(k, de).km
            user.distance_with_Bike=dis
            user.distance_with_Champion=dis
            user.distance_with_Ecovan=dis
            user.distance_with_Maruti=dis
            user.distance_with_Tata_ace_7FT=dis
            user.distance_with_Tata_ace_8FT=dis
            user.distance_with_Blero_8FT=dis
            # user.save()
            if dis:
                return redirect('kasim')


        if user.pick_point!=None and user.drop_point!=None and user!=None:
            if current_time > '05:00:00' and current_time < '14:59:59':
                if (p.extra1_distance >= dis or p.extra2_distance >=dis 
                    or  C.extra1_distance >= dis or C.extra2_distance >= dis or
                    E.extra1_distance >= dis or E.extra2_distance >= dis 
                    or  M.extra1_distance >= dis or T.extra2_distance >= dis
                    or  TT.extra1_distance >= dis or TT.extra2_distance >= dis
                    or  B.extra1_distance >= dis or B.extra2_distance >= dis or K.vehicle_type1
                    or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                        K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price1_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price1_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price1_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price1_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price1_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price1_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price1_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra2_distance >= dis or p.extra3_distance >=dis 
                   or  C.extra2_distance >= dis or C.extra3_distance >= dis or
                  E.extra2_distance >= dis or E.extra3_distance >= dis 
                  or  M.extra2_distance >= dis or T.extra3_distance >= dis
                  or  TT.extra2_distance >= dis or TT.extra3_distance >= dis
                  or  B.extra2_distance >= dis or B.extra3_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price2_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price2_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price2_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price2_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price2_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price2_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price2_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra3_distance >= dis or p.extra4_distance >=dis 
                   or  C.extra3_distance >= dis or C.extra4_distance >= dis or
                  E.extra3_distance >= dis or E.extra4_distance >= dis 
                  or  M.extra3_distance >= dis or T.extra4_distance >= dis
                  or  TT.extra3_distance >= dis or TT.extra4_distance >= dis
                  or  B.extra3_distance >= dis or B.extra4_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price3_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price3_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price3_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price3_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price3_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price3_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price3_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra4_distance >= dis or p.extra5_distance >=dis 
                   or  C.extra4_distance >= dis or C.extra5_distance >= dis 
                   or E.extra4_distance >= dis or E.extra5_distance >= dis 
                  or  M.extra4_distance >= dis or T.extra5_distance >= dis
                  or  TT.extra4_distance >= dis or TT.extra5_distance >= dis
                  or  B.extra4_distance >= dis or B.extra5_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price4_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price4_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price4_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price4_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price4_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price4_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price4_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                      
                elif (p.extra5_distance >= dis or p.extra6_distance >=dis 
                   or  C.extra5_distance >= dis or C.extra6_distance >= dis or
                  E.extra5_distance >= dis or E.extra6_distance >= dis 
                  or  M.extra5_distance >= dis or T.extra6_distance >= dis
                  or  TT.extra5_distance >= dis or TT.extra6_distance >= dis
                  or  B.extra5_distance >= dis or B.extra6_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price5_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price5_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price5_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price5_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price5_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price5_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price5_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra6_distance >= dis or dis or  
                    C.extra6_distance >= dis or  dis or 
                    E.extra6_distance >= dis or dis or  
                    M.extra6_distance >= dis or dis or  
                    TT.extra6_distance >= dis or  dis or  
                    B.extra6_distance >= dis or  dis or 
                    K.vehicle_type1 or K.vehicle_type2 or 
                    K.vehicle_type3 or K.vehicle_type4 or
                    K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):

                    fare1,f1=p.basefare+(dis - p.basekm)*p.price6_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price6_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price6_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price6_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price6_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price6_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price6_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
            
            
            elif current_time > '15:00:00' and current_time < '20:59:59':
                if (p.extra1_distance >= dis or p.extra2_distance >=dis 
                   or  C.extra1_distance >= dis or C.extra2_distance >= dis or
                  E.extra1_distance >= dis or E.extra2_distance >= dis 
                  or  M.extra1_distance >= dis or T.extra2_distance >= dis
                  or  TT.extra1_distance >= dis or TT.extra2_distance >= dis
                  or  B.extra1_distance >= dis or B.extra2_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price1_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price1_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price1_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price1_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price1_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price1_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price1_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra2_distance >= dis or p.extra3_distance >=dis 
                   or  C.extra2_distance >= dis or C.extra3_distance >= dis or
                  E.extra2_distance >= dis or E.extra3_distance >= dis 
                  or  M.extra2_distance >= dis or T.extra3_distance >= dis
                  or  TT.extra2_distance >= dis or TT.extra3_distance >= dis
                  or  B.extra2_distance >= dis or B.extra3_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price2_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price2_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price2_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price2_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price2_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price2_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price2_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra3_distance >= dis or p.extra4_distance >=dis 
                   or  C.extra3_distance >= dis or C.extra4_distance >= dis or
                  E.extra3_distance >= dis or E.extra4_distance >= dis 
                  or  M.extra3_distance >= dis or T.extra4_distance >= dis
                  or  TT.extra3_distance >= dis or TT.extra4_distance >= dis
                  or  B.extra3_distance >= dis or B.extra4_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price3_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price3_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price3_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price3_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price3_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price3_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price3_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra4_distance >= dis or p.extra5_distance >=dis 
                   or  C.extra4_distance >= dis or C.extra5_distance >= dis 
                   or E.extra4_distance >= dis or E.extra5_distance >= dis 
                  or  M.extra4_distance >= dis or T.extra5_distance >= dis
                  or  TT.extra4_distance >= dis or TT.extra5_distance >= dis
                  or  B.extra4_distance >= dis or B.extra5_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price4_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price4_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price4_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price4_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price4_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price4_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price4_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                      
                elif (p.extra5_distance >= dis or p.extra6_distance >=dis 
                   or  C.extra5_distance >= dis or C.extra6_distance >= dis or
                  E.extra5_distance >= dis or E.extra6_distance >= dis 
                  or  M.extra5_distance >= dis or T.extra6_distance >= dis
                  or  TT.extra5_distance >= dis or TT.extra6_distance >= dis
                  or  B.extra5_distance >= dis or B.extra6_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price5_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price5_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price5_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price5_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price5_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price5_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price5_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra6_distance >= dis or dis or  
                    C.extra6_distance >= dis or  dis or 
                    E.extra6_distance >= dis or dis or  
                    M.extra6_distance >= dis or dis or  
                    TT.extra6_distance >= dis or  dis or  
                    B.extra6_distance >= dis or  dis or 
                    K.vehicle_type1 or K.vehicle_type2 or 
                    K.vehicle_type3 or K.vehicle_type4 or
                    K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):

                    fare1,f1=p.basefare+(dis - p.basekm)*p.price6_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price6_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price6_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price6_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price6_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price6_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price6_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
            elif current_time > '21:00:00' and current_time < '04:59:59':
                if (p.extra1_distance >= dis or p.extra2_distance >=dis 
                    or  C.extra1_distance >= dis or C.extra2_distance >= dis or
                    E.extra1_distance >= dis or E.extra2_distance >= dis 
                    or  M.extra1_distance >= dis or T.extra2_distance >= dis
                    or  TT.extra1_distance >= dis or TT.extra2_distance >= dis
                    or  B.extra1_distance >= dis or B.extra2_distance >= dis or K.vehicle_type1
                    or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                        K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price1_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price1_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price1_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price1_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price1_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price1_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price1_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra2_distance >= dis or p.extra3_distance >=dis 
                   or  C.extra2_distance >= dis or C.extra3_distance >= dis or
                  E.extra2_distance >= dis or E.extra3_distance >= dis 
                  or  M.extra2_distance >= dis or T.extra3_distance >= dis
                  or  TT.extra2_distance >= dis or TT.extra3_distance >= dis
                  or  B.extra2_distance >= dis or B.extra3_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price2_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price2_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price2_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price2_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price2_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price2_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price2_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra3_distance >= dis or p.extra4_distance >=dis 
                   or  C.extra3_distance >= dis or C.extra4_distance >= dis or
                  E.extra3_distance >= dis or E.extra4_distance >= dis 
                  or  M.extra3_distance >= dis or T.extra4_distance >= dis
                  or  TT.extra3_distance >= dis or TT.extra4_distance >= dis
                  or  B.extra3_distance >= dis or B.extra4_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price3_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price3_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price3_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price3_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price3_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price3_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price3_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
             
                elif (p.extra4_distance >= dis or p.extra5_distance >=dis 
                   or  C.extra4_distance >= dis or C.extra5_distance >= dis 
                   or E.extra4_distance >= dis or E.extra5_distance >= dis 
                  or  M.extra4_distance >= dis or T.extra5_distance >= dis
                  or  TT.extra4_distance >= dis or TT.extra5_distance >= dis
                  or  B.extra4_distance >= dis or B.extra5_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price4_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price4_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price4_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price4_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price4_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price4_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price4_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                      
                elif (p.extra5_distance >= dis or p.extra6_distance >=dis 
                   or  C.extra5_distance >= dis or C.extra6_distance >= dis or
                  E.extra5_distance >= dis or E.extra6_distance >= dis 
                  or  M.extra5_distance >= dis or T.extra6_distance >= dis
                  or  TT.extra5_distance >= dis or TT.extra6_distance >= dis
                  or  B.extra5_distance >= dis or B.extra6_distance >= dis or K.vehicle_type1
                  or K.vehicle_type2 or K.vehicle_type3 or K.vehicle_type4 or
                     K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):
                    fare1,f1=p.basefare+(dis - p.basekm)*p.price5_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price5_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price5_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price5_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price5_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price5_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price5_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
                elif (p.extra6_distance >= dis or dis or  
                    C.extra6_distance >= dis or  dis or 
                    E.extra6_distance >= dis or dis or  
                    M.extra6_distance >= dis or dis or  
                    TT.extra6_distance >= dis or  dis or  
                    B.extra6_distance >= dis or  dis or 
                    K.vehicle_type1 or K.vehicle_type2 or 
                    K.vehicle_type3 or K.vehicle_type4 or
                    K.vehicle_type5 or K.vehicle_type6 or K.vehicle_type7):

                    fare1,f1=p.basefare+(dis - p.basekm)*p.price6_per_km , K.vehicle_type1
                    fare2,f2=C.basefare+(dis - C.basekm)*C.price6_per_km,K.vehicle_type2
                    fare3,f3=E.basefare+(dis - E.basekm)*E.price6_per_km,K.vehicle_type3
                    fare4,f4=M.basefare+(dis - M.basekm)*M.price6_per_km,K.vehicle_type4
                    fare5,f5=T.basefare+(dis - T.basekm)*T.price6_per_km,K.vehicle_type5
                    fare6,f6=TT.basefare+(dis - TT.basekm)*TT.price6_per_km,K.vehicle_type6
                    fare7,f7=B.basefare+(dis - B.basekm)*B.price6_per_km,K.vehicle_type7
                    user.total_price_Bike=fare1
                    user.total_price_Champion=fare2
                    user.total_price_Ecovan=fare3
                    user.total_price_Maruti=fare4
                    user.total_price_Tata_ace_7FT=fare5
                    user.total_price_Tata_ace_8FT=fare6
                    user.total_price_Blero_8FT=fare7
                    # user.save()
                    print("K2")
                    return response.Response({f1,fare1,fare2,fare3,fare4,fare5,fare6,fare7,f2,f3,f4,f5,f6,f7 }) 
                
             
             
             
            


