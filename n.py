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

# # veh_type = 'tata ace 7ft'
# veh_type='tata 407'

# now = datetime.datetime.now()
# current_time = now.strftime("%H:%M:%S")
# basefare = 350
# basekm = 3
# distance = 50 
# price_per_km = 28

# print(get_fare(veh_type, current_time, basefare, basekm, distance, price_per_km))





  
# import math
# R = 6373.0
# #radius of the Earth
# lat1 = math.radians(52.2296756)
# # coordinates
# lon1 = math.radians(21.0122287)
# lat2 = math.radians(52.406374)
# lon2 = math.radians(16.9251681)
# dlon = lon2 - lon1
# # change in coordinates
# dlat = lat2 - lat1
# a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
# #Haversine formula
# c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
# distance = R * c
# print(distance)

# Importing the great_circle module from the library
# import geopy
# from geopy.distance import great_circle
# from geopy.distance import geodesic
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="kasim")
# n=input("enter the first city")
# n1=input("enter the first city")
# location1 = geolocator.geocode(n)
# location2 = geolocator.geocode(n1)
# print(location1.address)
# print(location2.address)
# l1,l2=location1.latitude, location1.longitude
# print(l1,l2)
# l3,l4=location2.latitude, location2.longitude
# kolkata = (l1, l2)
# delhi = (l3,l4)
# print(geodesic(kolkata, delhi).km)

# for i in range(0,10):
#     for j in range(0,i-1):
#         print("*" , end="  ")
#     print("")   
# 
# 

a=10
b=10
print(id(a),"kasim")
print(id(b),"kasim")




# Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...








