from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class para(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,default=User.username)
    date=models.DateField(default=date.today,null=True,blank=True)
    write=models.TextField()
    