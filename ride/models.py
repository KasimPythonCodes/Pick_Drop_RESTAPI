from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rider_Trip(models.Model):
    basefare = models.FloatField()
    basekm = models.FloatField()
    price1_per_km = models.FloatField(blank=True , null=True)
    price2_per_km = models.FloatField(blank=True , null=True)
    price3_per_km = models.FloatField(blank=True , null=True)
    price4_per_km = models.FloatField(blank=True , null=True)
    price5_per_km = models.FloatField(blank=True , null=True)
    price6_per_km = models.FloatField(blank=True , null=True)
    extra1_distance = models.FloatField(blank=True , null=True)
    extra2_distance = models.FloatField(blank=True , null=True)
    extra3_distance = models.FloatField(blank=True , null=True)
    extra4_distance = models.FloatField(blank=True , null=True)
    extra5_distance = models.FloatField(blank=True , null=True)
    extra6_distance = models.FloatField(blank=True , null=True)


   

    
    

    def __str__(self):
        return str(self.basefare)

Truck=(
    ('tata 407','tata 407'),
    ('blero','blero'),
    )

class User_pick_form(models.Model):
    # admin=models.ForeignKey(Rider_Trip ,on_delete=models.CASCADE)
    select_truck_type=models.CharField(choices=Truck ,max_length=150)
    pick_point=models.CharField(max_length=256)
    drop_point=models.CharField(max_length=256)
    distance=models.FloatField(max_length=256 , blank=True , null=True)
    total_price=models.FloatField(max_length=256 , blank=True , null=True)

   

    def __str__(self):
        return self.pick_point

# class Car_Model(models.Model):
#     basefare = models.FloatField()
#     basekm = models.FloatField()
#     distance = models.FloatField(blank=True)
#     price_per_km = models.FloatField(blank=True)
#     total_price=models.FloatField(max_length=256 , blank=True)

# class Car_Model(models.Model):
#     basefare = models.FloatField()
#     basekm = models.FloatField()
#     distance = models.FloatField(blank=True)
#     price_per_km = models.FloatField(blank=True)
#     total_price=models.FloatField(max_length=256 , blank=True)

# class Car_Model(models.Model):
#     basefare = models.FloatField()
#     basekm = models.FloatField()
#     distance = models.FloatField(blank=True)
#     price_per_km = models.FloatField(blank=True)
#     total_price=models.FloatField(max_length=256 , blank=True)

# class Car_Model(models.Model):
#     basefare = models.FloatField()
#     basekm = models.FloatField()
#     distance = models.FloatField(blank=True)
#     price_per_km = models.FloatField(blank=True)
#     total_price=models.FloatField(max_length=256 , blank=True)

# class Car_Model(models.Model):
#     basefare = models.FloatField()
#     basekm = models.FloatField()
#     distance = models.FloatField(blank=True)
#     price_per_km = models.FloatField(blank=True)
#     total_price=models.FloatField(max_length=256 , blank=True)
