from django.shortcuts import render
from .models import CoffeeHouse 
from django.views.generic import ListView,CreateView,DetailView
from .forms import AddCoffeHouseForm
# Create your views here.


class ListCoffeeHouse(ListView):
    model = CoffeeHouse
    template_name = 'coffee_house/coffeehouse_list.html'
    context_object_name = 'coffeehouse'
    

class AddCoffeeHouse(CreateView):
    form_class = AddCoffeHouseForm
    template_name = 'coffee_house/addcoffeehouse.html'
    context_object_name = 'owners'
    

class CoffeeHouseView(DetailView):
    model = CoffeeHouse
    slug_url_kwarg = 'title'
    