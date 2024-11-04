from django.urls import path
from .views import AddCoffeeHouse,ListCoffeeHouse,CoffeeHouseEditDelete
from .views_func import get_list_coffeehouse, get_detail_coffeehouse
urlpatterns = [
    path('', get_list_coffeehouse, name = 'list_coffee_house'),
    path('add_coffee_house/', AddCoffeeHouse.as_view()),
    path('<slug:slug>/', get_detail_coffeehouse, name = 'detail_coffee_house'),
    path('<slug:slug>/edit/', CoffeeHouseEditDelete.as_view())
]