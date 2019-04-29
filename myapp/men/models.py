from django.db import models
import numpy as np






# Create your models here.
class product(models.Model):
    img=models.ImageField(
        upload_to='images/men/'
    )
    product_name = models.CharField(max_length=50,null=False)
    product_type = models.CharField(max_length=50,null=False)
    garuntee = models.IntegerField(null=False)
    pri = models.IntegerField(null=False)
    catagories = models.CharField(max_length=150,default='',choices=(('Digital','Digital'),('Analogue','Analogue'),('Automatic','Automatic'),('Pilot','Pilot'),('Chronograph','Chronograph'),('Diving','Diving'),('Mechanical','Mechanical'),('Smart','Smart'),('Luxury','Luxury')))
    size = models.CharField(max_length=50,default='',choices=(('M','M'),('L','L'),('one-size','one-size'),('pack','pack')))
    price_choice = models.CharField(max_length=150,default='',choices=(('less than 500','less than 500'),('500-1000','500-1000'),('1000-1500','1000-1500'),('1500-5000','1500-5000'),('5000_more','5000_more')))

    disc = models.CharField(max_length=50,null=False,default='')
    
       
    def __str__(self):
        return self.product_name



    def __int__(self):
        return self.pri  + self.size + self.price_choice + self.disc 


class wishlist(models.Model):
    product_name = models.CharField(max_length=50,null=False)
    product_type = models.CharField(max_length=50,null=False)
    pri = models.IntegerField(null=False)
    catagories = models.CharField(max_length=150,default='',choices=(('Digital','Digital'),('Analogue','Analogue'),('Automatic','Automatic'),('Pilot','Pilot'),('Chronograph','Chronograph'),('Diving','Diving'),('Mechanical','Mechanical'),('Smart','Smart'),('Luxury','Luxury')))
    size = models.CharField(max_length=50,default='',choices=(('M','M'),('L','L'),('one-size','one-size'),('pack','pack')))
    disc = models.IntegerField(null=False,default='')

    def __int__(self):
        return self.product_name + ' ' + self.pri  + self.size +  self.disc
    

class payment(models.Model):
    product_name = models.ForeignKey(product,on_delete=models.CASCADE,related_name=None,default='')
    paytype = models.TextField(max_length=50,null=False,default='')
    paytype = models.CharField(max_length=50,choices=(('credit card','credit card'),('debit card','debit card'),('net banking','net banking')))
    bank_name = models.CharField(max_length=50,null=False)
    Account_number = models.IntegerField(null=False)
    password = models.CharField(max_length=50,null=False)

    
class new_review(models.Model):
    product_name = models.ForeignKey(product,on_delete=models.CASCADE,related_name=None,default='')
    star = models.CharField(max_length=50,default='')

    def average_rating(self):
        all_ratings = map(lambda x: x.star,new_review)
        return np.mean(all_ratings)
     
    def __int__(self):
        return self.star   

   





# numpy mate 
# class Product(models.Model):
#     name = models.CharField(max_length=200)
    
#     def average_rating(self):
#         all_ratings = map(lambda x: x.rating, self.review_set.all())
#         return np.mean(all_ratings)
        
#     def __str__(self):
#         return self.name

# class Review(models.Model):
#     RATING_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     )
#     product = models.ForeignKey(Product)
#     pub_date = models.DateTimeField('date published')
#     user_name = models.CharField(max_length=100)
#     comment = models.CharField(max_length=200)
#     rating = models.IntegerField(choices=RATING_CHOICES)

       