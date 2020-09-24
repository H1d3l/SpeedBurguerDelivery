from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,primary_key=True)
    email = models.EmailField(max_length=200)


    def __str__(self):
        return self.username