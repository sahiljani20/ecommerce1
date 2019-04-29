from django.db import models
from myapp.men.models import *


# Create your models here.


class login(models.Model):
    user_name = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)

class wishlist(models.Model):
    product_name = models.CharField(max_length=50,null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.product_name


class discount(models.Model):
    product_name = models.ForeignKey(wishlist,on_delete=models.CASCADE,related_name=None,null= True)
    percentage = models.IntegerField(default='')
    # last_price = product price - discount

class rating(models.Model):
    star = models.CharField(max_length=50,default='')


class contacts(models.Model):
    Name = models.CharField(max_length=50,null=False)
    Email = models.EmailField(max_length=50,null=False)
    Subject = models.CharField(max_length=250,null=False)
    Message = models.CharField(max_length=50,null=False)
    