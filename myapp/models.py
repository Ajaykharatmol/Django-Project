from django.db import models

# Create your models here.

class Category(models.Model):  
    Category_Name = models.CharField(max_length=20)
    Category_Type = models.CharField(max_length=20)
    

    class Meta:  
        db_table = "Category" 

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    uemail = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.uname+" "+self.password

    class Meta:
        db_table = "UserInfo"
    




class Products(models.Model):
    Product_Name = models.CharField(max_length=20)
    Product_Image = models.CharField(max_length=20)
    Product_Price = models.FloatField(default=12000)
    Product_Description = models.CharField(max_length=20)
    dept = models.ForeignKey(Category, on_delete=models.CASCADE)


class Cart(models.Model):
    unique_together = (('emp', 'user'),)
    emp = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = "Cart"

class Payment(models.Model):
    cardno = models.IntegerField(default=100)
    cvvno = models.IntegerField(default=100)
    expiryDate = models.CharField(max_length=20)
    amount = models.FloatField(default=100)

    class Meta:
        db_table = "Payment"
