from django.db import models

# Create your models here.

class Product(models.Model):
    TYPE_PRODUCT = [
        ('Hamburguer', "Hamburguer"),
        ('Bebidas', "Bebidas"),
        ('Pasteis', "Pasteis"),
        ('Outros', "Outros"),
    ]

    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(default = 0,decimal_places=2, max_digits=8)
    type_product = models.CharField(max_length=20, choices=TYPE_PRODUCT,default='Hamburguer')
    image = models.ImageField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




class Combo(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(default = 0,decimal_places=2, max_digits=8)
    image = models.ImageField(default = 'defalt.png',blank=True)

    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
