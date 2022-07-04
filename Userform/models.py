from django.db import models
from django.contrib.auth.models import User
from ride.models import*
from Userform.models import*
# Create your models here.
#

 
class PICKFORM(models.Model):
    # user=models.ForeignKey(User , on_delete=models.CASCADE)
    # user_vehicle=models.ForeignKey(User , on_delete=models.CASCADE)
    pick_point=models.CharField(max_length=256)
    drop_point=models.CharField(max_length=256)
    distance=models.FloatField(max_length=256 , blank=True , null=True)
    # price_t=models.FloatField(max_length=256 , blank=True , null=True)
    
    # total_price_Bike=models.FloatField(max_length=256 , blank=True , null=True)
    # distance_with_Champion=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Champion=models.FloatField(max_length=256 , blank=True , null=True) 
    # distance_with_Ecovan=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Ecovan=models.FloatField(max_length=256 , blank=True , null=True)
    # distance_with_Maruti=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Maruti=models.FloatField(max_length=256 , blank=True , null=True)
    # distance_with_Tata_ace_7FT=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Tata_ace_7FT=models.FloatField(max_length=256 , blank=True , null=True)
    # distance_with_Tata_ace_8FT=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Tata_ace_8FT=models.FloatField(max_length=256 , blank=True , null=True)
    # distance_with_Blero_8FT=models.FloatField(max_length=256 , blank=True , null=True)
    # total_price_Blero_8FT=models.FloatField(max_length=256 , blank=True , null=True)
    objects=models.Manager()
    def __str__(self):
        return self.pick_point 

class Profile(models.Model):
    user = models.OneToOneField(to=PICKFORM,on_delete=models.CASCADE)        