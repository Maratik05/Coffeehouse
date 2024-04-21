from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import FormView,ListView,UpdateView,DeleteView
from .forms import AddOwnerForm
from coffee_house.models import CoffeeHouse
from owners.models import Owner
from django.middleware.csrf import get_token
# Create your views here.



class AddOwnerView(FormView):
    template_name = 'owners/addowner.html'
    form_class = AddOwnerForm
    success_url = '/owners/id/'
    

    # def csrf_token(request):
    #     csrf_token = get_token(request)
    

class CoffeHouseOwner(ListView):
    model = CoffeeHouse
    template_name = 'owners/ownersprofile.html'
    context_object_name = 'coffeehouse'

    def get_queryset(self):
        return CoffeeHouse.objects.filter(owner_id = self.kwargs['owner_id'])

class EditDeleteOwner(UpdateView,DeleteView):
    model = Owner
    template_name = 'editdeleteowner.html'

        


    

