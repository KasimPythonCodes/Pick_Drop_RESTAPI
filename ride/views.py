
from rest_framework import serializers
from django.shortcuts import render ,HttpResponse
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
# geopy.location.Location.address
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView

# UserSerializer

class RegisterAPI(GenericAPIView):
    serializer_class = UserSerializerForm
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        for p in Rider_Trip.objects.all():
            print(p.price1_per_km,"kasim")
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # print(serializer,"$$$$$$$$$")
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        geolocator = Nominatim(user_agent="kasim",timeout=10)
        n=user.pick_point
        n1=user.drop_point
        # print(n,"1",n1,"2" ,"PICK &&*B DROP")
        location1 = geolocator.geocode(n) 
        location2 = geolocator.geocode(n1)
        u1=user.pick_point=location1 
        u2=user.drop_point=location2 
        #    return JSONResponse({'error' : str(e)},status=500)
            # return response.Response("kkkkkkk")
        # print(u1,"pick location and " , u2 ,"drop location","mmmmmmmmmmmmm")
        # print(location1,"location 11","000000000000")
        # print(location2,"location 22","99999999999999")
        if u1 and u2:
            l1,l2=u1.latitude, u1.longitude
            l3,l4=u2.latitude, u2.longitude
            k = (l1, l2)
            de= (l3,l4)
            # print(great_circle(k, de).km , "kasimsaifi @@@@@@@@@@@@@######")
            dis=great_circle(k, de).km
            user.distance=dis
            user.save()
            # stu=User_pick_form(
            # id=user,
            # )
            # stu.save()
        if user.select_truck_type!=None and user.pick_point!=None and user.drop_point!=None and user!=None:
            if current_time > '05:00:00' and current_time < '14:59:59':
                if p.extra1_distance >= dis or p.extra2_distance >= dis:
                    fare=p.basefare+(dis - p.basekm)*p.price1_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"1")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                elif  p.extra2_distance >= dis or p.extra3_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price2_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"2")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                elif  p.extra3_distance >= dis or p.extra4_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price3_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"3")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                
                elif  p.extra4_distance >= dis or p.extra5_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price4_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"4")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                elif  p.extra5_distance >= dis or p.extra6_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price5_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"5")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}")   
                
                elif p.extra6_distance <= dis or dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price6_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"6")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}")    
            elif current_time > '15:00:00' and current_time < '20:59:59':
                    if p.extra1_distance >= dis or p.extra2_distance >= dis:
                        fare=p.basefare+(dis - p.basekm)*p.price1_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"1")
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                    elif  p.extra2_distance >= dis or p.extra3_distance >= dis:   
                        fare=p.basefare+(dis - p.basekm)*p.price2_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"2")
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                    elif  p.extra3_distance >= dis or p.extra4_distance >= dis:   
                        fare=p.basefare+(dis - p.basekm)*p.price3_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"3")
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                    
                    elif  p.extra4_distance >= dis or p.extra5_distance >= dis:   
                        fare=p.basefare+(dis - p.basekm)*p.price4_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"4" )
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                    elif  p.extra5_distance >= dis or p.extra6_distance >= dis:   
                        fare=p.basefare+(dis - p.basekm)*p.price5_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"5")
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}")   
                
                    elif p.extra6_distance <= dis or dis:   
                        fare=p.basefare+(dis - p.basekm)*p.price6_per_km
                        user.total_price=fare
                        user.save()
                        print(fare,"6")
                        return response.Response(f"{'Total Fare',fare ,'Time', current_time}")  
            elif current_time > '21:00:00' and current_time < '04:59:59':
                if p.extra1_distance >= dis or p.extra2_distance >= dis:
                    fare=p.basefare+(dis - p.basekm)*p.price1_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"1")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                elif  p.extra2_distance >= dis or p.extra3_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price2_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"2")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                elif  p.extra3_distance >= dis or p.extra4_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price3_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"3")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 
                
                elif  p.extra4_distance >= dis or p.extra5_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price4_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"4")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}") 

                elif  p.extra5_distance >= dis or p.extra6_distance >= dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price5_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"5")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}")   
                
                elif p.extra6_distance <= dis or dis:   
                    fare=p.basefare+(dis - p.basekm)*p.price6_per_km
                    user.total_price=fare
                    user.save()
                    print(fare,"6")
                    return response.Response(f"{'Total Fare',fare ,'Time', current_time}")


        # return Response({
        # # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "user": UserSerializerForm(user, context=self.get_serializer_context()).data,
        # # "token": AuthToken.objects.create(user)[1]
        # })


# class index(ModelViewSet):
#     serializer_class=Testrider
#     def get_queryset(self):
#         post=User_pick_form.objects.all()
#         return post
#     def create(self,request,*args, **kwargs):
#         post_data=request.data
#         for p in Rider_Trip.objects.all():
#             print(p.distance,"kasim")
#         now = datetime.datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         try:
#          user=User_pick_form.objects.create(pick_point=post_data['pick_point'],drop_point=post_data['drop_point'] ,select_truck_type=post_data['select_truck_type']) #first db data    
#         except TypeError:
#             raise TypeError("kasim")
#         geolocator = Nominatim(user_agent="kasim",timeout=10)
#         n=user.pick_point
#         n1=user.drop_point
#         # print(n,"1",n1,"2" ,"PICK &&*B DROP")
#         location1 = geolocator.geocode(n) 
#         location2 = geolocator.geocode(n1)
#         u1=user.pick_point=location1 
#         u2=user.drop_point=location2 
#         #    return JSONResponse({'error' : str(e)},status=500)
#             # return response.Response("kkkkkkk")
#         print(u1,"pick location and " , u2 ,"drop location","mmmmmmmmmmmmm")
#         print(location1,"location 11","000000000000")
#         print(location2,"location 22","99999999999999")
#         if  location1==None or location2==None:
#              raise serializers.ValidationError({'name': 'Please enter a valid pick  and drop locations.'})
#         # if u1==None and u2==None:
#         # s1=location1.address
#         # s2=location2.address
#         # s1=u1.address
#         # s2=u2.address
#         # print(s1,"@@@@@",s2)
#         # if location1 and location2:
#         #     l1,l2=location1.latitude, location1.longitude
#         #     l3,l4=location2.latitude, location2.longitude
#         if u1 and u2:
#             l1,l2=u1.latitude, u1.longitude
#             l3,l4=u2.latitude, u2.longitude
#             k = (l1, l2)
#             de= (l3,l4)
#             print(great_circle(k, de).km , "kasimsaifi @@@@@@@@@@@@@######")
#             dis=great_circle(k, de).km
#             p.distance=dis
#             user.save() 
#         else:
#             return response.Response({'msg':"enter pick & drop Location"})  
#         if user.select_truck_type!=None and user.pick_point!=None and user.drop_point!=None and user!=None:
#             if current_time > '05:00:00' and current_time < '14:59:59':
#                     fare=p.basefare+(dis - p.basekm)*p.price_per_km
#                     p.total_price=fare
#                     p.save()
#                     print(fare,"kasim1")
#                     return response.Response(f"{'Total Fare',fare ,'Time', current_time}")   
#             elif current_time > '15:00:00' and current_time < '20:59:59':
#                 fare=p.basefare+(dis - p.basekm)*p.price_per_km
#                 p.total_price=fare
#                 p.save()
#                 print(fare,"kasim1")
#                 return response.Response(f"{'Total Fare',fare ,'Time', current_time}")   
#             elif current_time > '21:00:00' and current_time < '04:59:59':
#                 fare=p.basefare+(dis - p.basekm)*p.price_per_km
#                 p.total_price=fare
#                 p.save()
#                 print(fare,"kasim1")
#                 return response.Response(f"{'Total Fare',fare ,'Time', current_time}")  
#         else:
#             return response.Response({"msg":"Please Enter The Valid credential"})

  


























# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         fm=testapi1(request.POST or None)
#         basefare=request.POST.get('basefare')
#         basekm=request.POST.get('basekm')
#         distance=request.POST.get('distance')
#         price_per_km=request.POST.get('price_per_km')
#         user1=Rider_Trip(basefare=basefare,basekm=basekm ,distance=distance ,price_per_km=price_per_km)
#         print(user1,"USER!@#$")
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm=testapi1(None)        
#     return render(request, 'index.html' , {'fm':fm })    

# def testapiclass(request):
#     if request.method == 'POST':
#         form=testapi(request.POST or None)
#         for p in Rider_Trip.objects.all():
#             print(p,"kasim")
#         pick=request.POST.get('pick_point')
#         drop=request.POST.get('drop_point')
#         vehicle_type=request.POST.get('select_truck_type')
#         now = datetime.datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         user=User_pick_form(pick_point=pick ,drop_point=drop ,select_truck_type=vehicle_type)
#         if user.select_truck_type and user.pick_point and user.drop_point and user!=None:
#             #    fare = p.basefare+(p.distance - p.basekm)*p.price_per_km  
#             #    print(fare)      
#             if current_time > '05:00:00' and current_time < '14:59:59':
#                 fare=p.basefare+(p.distance - p.basekm)*p.price_per_km
#                 print(fare,"kasim1")
#             elif current_time > '15:00:00' and current_time < '20:59:59':
#                fare = p.basefare+(p.distance - p.basekm)*p.price_per_km
#                print(fare ,"kasim2")
#                return fare
#             elif current_time > '21:00:00' and current_time < '04:59:59':
#                fare = p.basefare+(p.distance - p.basekm)*p.price_per_km  
#                print(fare ,"kasim3")           
#                return fare
#         # if user.select_truck_type==request.user:
#         #    if current_time > '05:00:00' and current_time < '14:59:59':
#         #        fare = p.basefare+(p.distance-p.basekm)*p.price_per_km
#         #        print(fare ,"kasim1")
#         #        return fare
#         #    elif current_time > '15:00:00' and current_time < '20:59:59':
#         #        fare = p.basefare+(p.distance-p.basekm)*p.price_per_km
#         #        print(fare ,"kasim2")
#         #        return fare
#         #    elif current_time > '21:00:00' and current_time < '04:59:59':
#         #        fare = p.basefare+(p.distance-p.basekm)*p.price_per_km  
#         #        print(fare ,"kasim3")          
#         #        return fare
#         # if user.select_truck_type and user.pick_point and user.drop_point and user!=None:
#         #     fare=p.basefare+(p.distance - p.basekm)*p.price_per_km
#         if form.is_valid():
#             form.save()
#     else:
#         form=testapi(None) 
#         # if user.select_truck_type and user.pick_point and user.drop_point and user!=None:
#         #     fare=None
#     return render(request, 'index.html' , {'form':form })    


# import datetime
# def get_fare(veh_type, current_time, basefare, basekm, distance, price_per_km):
#     if veh_type == veh_type:
#         if current_time > '05:00:00' and current_time < '14:59:59':
#             fare = basefare+(distance-basekm)*price_per_km
#         if current_time > '15:00:00' and current_time < '20:59:59':
#             fare = basefare+(distance-basekm)*price_per_km
#         if current_time > '21:00:00' and current_time < '04:59:59':
#             fare = basefare+(distance-basekm)*price_per_km            
#         return fare


















# class index(ModelViewSet):
#     serializer_class =Testrider
#     def get_queryset(self):
#         posts = User_pick_form.objects.all()
#         return posts
#     def create(self,request ,*args, **kwargs):
#         post_data=request.data
#         user=User_pick_form(select_truck_type=post_data['select_truck_type'],pick_point=post_data['pick_point'],drop_point=post_data['drop_point']) 
#         user.save() 
#         serializer=Testrider(user)
#         return Response(serializer.data) 
   


    # def get_fare(self,veh_type, current_time, basefare, basekm, distance, price_per_km):
    #     if veh_type == veh_type:
    #             if current_time > '05:00:00' and current_time < '14:59:59':
    #                 fare = basefare+(distance-basekm)*price_per_km
    #             if current_time > '15:00:00' and current_time < '20:59:59':
    #                 fare = basefare+(distance-basekm)*price_per_km
    #             if current_time > '21:00:00' and current_time < '04:59:59':
    #                 fare = basefare+(distance-basekm)*price_per_km            
    #             return fare

    #     veh_type = 'tata ace 7ft'
    #     now = datetime.datetime.now()
    #     current_time = now.strftime("%H:%M:%S")
    #     basefare = 350
    #     basekm = 3
    #     distance = 50
    #     price_per_km = 28



















# def get_fare(veh_type, current_time, basefare, basekm, distance, price_per_km):
#     if veh_type == veh_type:
#         if current_time > '05:00:00' and current_time < '14:59:59':
#             fare = basefare+(distance-basekm)*price_per_km
#         if current_time > '15:00:00' and current_time < '20:59:59':
#             fare = basefare+(distance-basekm)*price_per_km
#         if current_time > '21:00:00' and current_time < '04:59:59':
#             fare = basefare+(distance-basekm)*price_per_km            
#         return fare

# veh_type = 'tata ace 7ft'
# now = datetime.datetime.now()
# current_time = now.strftime("%H:%M:%S")
# basefare = 350
# basekm = 3
# distance = 50
# price_per_km = 28

# get_fare(veh_type, current_time, basefare, basekm, distance, price_per_km)


