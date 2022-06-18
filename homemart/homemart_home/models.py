from django.db import models
class for_registration(models.Model):
    name = models.CharField(max_length=200,null=False)
    password= models.CharField(max_length=200,null=False)
    phone_nu=models.CharField(max_length=10,null=False,unique=True)
    loc=models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.phone_nu
class Product(models.Model):
    productname = models.CharField(max_length=200)
    discription = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    Cartid=models.CharField(max_length=10,null=True)
# Create your models here.
class customer_details(models.Model):
    f_name=models.CharField(max_length=25,null=False)
    l_name=models.CharField(max_length=25,null=False)
    phone_no=models.CharField(max_length=10,null=False)
    email=models.CharField(max_length=50,null=False)
    country=models.CharField(max_length=25,null=False)
    Address1=models.CharField(max_length=75,null=False)
    Address2=models.CharField(max_length=75,null=False)
    Post_Zip=models.IntegerField(max_length=10,null=False)
    Town_City=models.CharField(max_length=25,null=False)
    Additional=models.TextField(max_length=100,null=False)
'''class Items(models.Model):
    Item_name=models.CharField(max_length=35,null=False)
    quantity=models.IntegerField(max_length=20,null=False)
    price=models.CharField(max_length=10000,null=False)
    total_price=models.IntegerField(max_length=50000,null=False)'''
class cart(models.Model):
    Cartid=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=11)
    shopName=models.CharField(max_length=100,null=True)
    shopid=models.CharField(max_length=25,null=True)
class shops(models.Model):
    cartid=models.CharField(max_length=10,null=True)
    price=models.CharField(max_length=10,null=True)
    shopid=models.CharField(max_length=25)
    shopname=models.CharField(max_length=100)