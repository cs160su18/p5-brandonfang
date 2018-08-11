from django.db import models
class User(models.Model):
    user_id = models.CharField(max_length=15)
    password = models.CharField(max_length=15)  
    budget = models.DecimalField(max_digits = 8, decimal_places = 2)

class ShopList(models.Model):
    item = models.CharField(max_length=30)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Group(models.Model):
    established = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 200)

class Activity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
