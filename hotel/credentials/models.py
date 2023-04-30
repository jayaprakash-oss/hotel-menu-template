from django.db import models

# Create your models here.
class credentials(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Username=models.CharField(max_length=13)
    Password=models.CharField(max_length=50,default='NA')
    Email=models.CharField(max_length=40,default='NA')
   
