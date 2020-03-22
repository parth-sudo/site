from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(default='orange.jpg')
    date_of_account_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Paytm(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return self.username