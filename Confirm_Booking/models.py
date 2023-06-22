from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Confirm_Booking(models.Model):
    # user=models.ForeignKey(User , on_delete=models.CASCADE)
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    pick_point=models.CharField(max_length=256, blank=True ,null=True)
    drop_point=models.CharField(max_length=256, blank=True ,null=True)
    price=models.FloatField()
    distance=models.FloatField()
    vehicle=models.CharField(max_length=256, blank=True ,null=True)
    objects=models.Manager()
    
    
    def __str__(self):
        return str(self.user.username )       