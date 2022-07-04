from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Bike_Trip(models.Model):
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
    objects=models.Manager()
    def __str__(self):
        return str(self.basefare)


class Champion_Trip(models.Model):
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
    objects=models.Manager()

    def __str__(self):
        return str(self.basefare)


class Ecovan_Trip(models.Model):
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
    objects=models.Manager() 
    def __str__(self):
        return str(self.basefare)


class Maruti_suzuki_super_carry_Trip(models.Model):
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
    objects=models.Manager()

    def __str__(self):
        return str(self.basefare)


class Tata_ace_7FT_Trip(models.Model):
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
    objects=models.Manager()
    def __str__(self):
        return str(self.basefare)


class Tata_ace_8FT_Trip(models.Model):
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
    objects=models.Manager() 
    def __str__(self):
        return str(self.basefare)


class Blero_8FT_Trip(models.Model):
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
    objects=models.Manager()


    def __str__(self):
        return str(self.basefare)

# Truck=(
#     ('tata 407','tata 407'),
#     ('blero','blero'),)

class Vehicle_type(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    vehicle=models.CharField(max_length=256)
    
    
    # vehicle_type2=models.CharField(max_length=256)
    # vehicle_type3=models.CharField(max_length=256)
    # vehicle_type4=models.CharField(max_length=256)
    # vehicle_type5=models.CharField(max_length=256)
    # vehicle_type6=models.CharField(max_length=256)
    # vehicle_type7=models.CharField(max_length=256)
    # total_price=models.FloatField(max_length=256 , blank=True , null=True)
    objects=models.Manager()
    def __str__(self):
        return self.vehicle
    


             