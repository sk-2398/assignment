from django.db import models

# Create your models here.
class UserDB(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250,primary_key=True)
    gender=models.CharField(max_length=100)
    salary=models.CharField(max_length=100, null=True,blank=True)
    age=models.CharField(max_length=100,null=True,blank=True)
    
    