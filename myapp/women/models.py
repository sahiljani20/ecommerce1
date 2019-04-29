from django.db import models
from myapp.home.models import *

# Create your models here.
class wo_product(models.Model):
    img = models.ImageField(
        upload_to='images/women/'
    )
    product_name = models.CharField(max_length=50,null=False)
    product_type = models.CharField(max_length=50,null=False)
    garuntee = models.IntegerField(null=False)
    pri = models.IntegerField(null=False)
    catagories = models.CharField(max_length=150,default='',choices=(('Digital','Digital'),('Analogue','Analogue'),('Automatic','Automatic'),('Pilot','Pilot'),('Chronograph','Chronograph'),('Diving','Diving'),('Mechanical','Mechanical'),('Smart','Smart'),('Luxury','Luxury')))
    size = models.CharField(max_length=150,default='',choices=(('M','M'),('L','L'),('one-size','one-size'),('pack','pack')))
    price_choice = models.CharField(max_length=150,default='',choices=(('less than 500','less than 500'),('500-1000','500-1000'),('1000-1500','1000-1500'),('1500-5000','1500-5000'),('5000_more','5000_more')))

    disc = models.CharField(max_length=50,null=False,default='')
    

    def __int__(self):
        return self.product_name + ' ' + self.catagories + self.size + self.pri

class discount(models.Model):
    product_name = models.ForeignKey(wo_product,on_delete=models.CASCADE,related_name=None)
    percentage = models.IntegerField(default='')
    # last_price = product price - discount


class wowishlist(models.Model):
    product_name = models.CharField(max_length=50,null=False)
    product_type = models.CharField(max_length=50,null=False)
    pri = models.IntegerField(null=False)
    catagories = models.CharField(max_length=150,default='',choices=(('Digital','Digital'),('Analogue','Analogue'),('Automatic','Automatic'),('Pilot','Pilot'),('Chronograph','Chronograph'),('Diving','Diving'),('Mechanical','Mechanical'),('Smart','Smart'),('Luxury','Luxury')))
    size = models.CharField(max_length=50,default='',choices=(('M','M'),('L','L'),('one-size','one-size'),('pack','pack')))
    disc = models.IntegerField(null=False,default='')

    def __int__(self):
        return self.product_name + ' ' + self.pri  + self.size +  self.disc
    
# class choices(models.Model):
#     choices=((6, 'credit card'),(7,'debit card'),(8,'net banking'),)

class payment(models.Model):
    product_name = models.ForeignKey("wo_product",on_delete=models.CASCADE,related_name=None)
    paytype = models.TextField(max_length=50,null=False,default='')
    paytype = models.CharField(max_length=50,choices=((6, 'credit card'),(7,'debit card'),(8,'net banking')))
    bank_name = models.CharField(max_length=50,null=False)
    Account_number = models.IntegerField(null=False)
    password = models.CharField(max_length=50,null=False)

class review(models.Model):
    product_name = models.CharField(max_length=50,default='')
    star = models.IntegerField(null=False,default='')
    star = models.CharField(max_length=50,choices=(('1','one'),('2','two'),('3','three'),('4','four'),('5','five'))) 
    comment = models.CharField(max_length=1000,null=False)
