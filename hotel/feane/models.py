from django.db import models

# Create your models here.
# class description:
#     id:int
#     iimg:str
#     mtitle:str
#     desc:str
#     price:int

class description(models.Model):
    
    
    mtitle=models.CharField(max_length=30)
    iimg=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    desc=models.CharField(max_length=100,default='NA')
    
   #cart models
class Product(models.Model):
     
    name=models.CharField(max_length=30)
    price=models.IntegerField(max_length=100)
    quantity=models.IntegerField(max_length=5)
    image=models.ImageField(upload_to='pics') 