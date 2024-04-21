from django.contrib import admin
from .models import CoffeeHouse,Owner,MenuItem,Menu
# Register your models here.
admin.site.register(CoffeeHouse)
admin.site.register(Owner)
admin.site.register(Menu)
admin.site.register(MenuItem)
