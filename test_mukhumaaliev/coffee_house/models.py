from django.db import models
from owners.models import Owner

# Create your models here.

    
class CoffeeHouse(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название кофейни')
    schedule = models.CharField(max_length=100, verbose_name='График работы')
    create_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class Menu(models.Model):
    name = models.CharField(max_length=100)
    coffeehouse = models.ForeignKey(CoffeeHouse,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    volume = models.IntegerField()
    UNIT_CHOICES = [
        ('ml', "мл"),
        ('l', "л"),
        ('gr', "гр"),
        ('кг', "kg")
    ] 
    unit = models.CharField(choices=UNIT_CHOICES,max_length=50)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/img', blank=True)

    def __str__(self):
        return self.name