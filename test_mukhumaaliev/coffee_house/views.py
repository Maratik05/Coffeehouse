from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CoffeeHouse,Owner 
from django import views
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,FormView
from .forms import AddCoffeHouseForm
from .models import CoffeeHouse

# Create your views here.


class ListCoffeeHouse(ListView):
    model = CoffeeHouse
    template_name = 'coffee_house/coffeehouse_list.html'
    context_object_name = 'coffeehouse'
    

class AddCoffeeHouse(CreateView):
    form_class = AddCoffeHouseForm
    template_name = 'coffee_house/addcoffeehouse.html'
    context_object_name = 'owners'

    
class CoffeeHouseUpdate(UpdateView):
    fields = ['all']
class CoffeeHouseDelete(DeleteView):
    fields = ['all']
    success_url = reverse_lazy('coffeehouse_list.html')



class CoffeeHouseEditDelete(CoffeeHouseUpdate, CoffeeHouseDelete):
    model = CoffeeHouse
    template_name = 'coffeehouseeditdelete.html'
    slug_url_kwarg = 'title'



def get_owner(request, owner_id):
    coffeehouse = CoffeeHouse.objects.filter(owner_id= owner_id)
    owners = Owner.objects.all()
    owner = Owner.objects.get(pk=owner_id)
    return render(request, 'coffeehouse_detail.html', {'coffeehouse': coffeehouse, 'owners': owners, 'owner': owner})
    