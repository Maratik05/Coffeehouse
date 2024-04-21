from django.urls import path
from .views import AddCoffeeHouse,ListCoffeeHouse,CoffeeHouseView
urlpatterns = [
    path('', ListCoffeeHouse.as_view()),
    path('add_coffee_house/', AddCoffeeHouse.as_view()),
    path('<slug:slug>', CoffeeHouseView.as_view())
]