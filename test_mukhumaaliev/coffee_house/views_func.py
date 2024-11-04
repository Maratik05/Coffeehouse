from django.shortcuts import render,redirect, get_object_or_404
from .models import CoffeeHouse,Owner, Menu


def get_list_coffeehouse(request):
    coffeehouse = CoffeeHouse.objects.filter()
    
    context = {
        'coffeehouse': coffeehouse,
        
        
    }

    return render(request, 'coffee_house/coffeehouse_list.html', context= context)


def get_detail_coffeehouse(request,slug):
    coffeehouse = get_object_or_404(CoffeeHouse, slug = slug)
    menu = Menu.objects.all()
    context = { 
        'coffeehouse': coffeehouse,
        'menu': menu
    }
    return render(request, 'coffee_house/coffeehouse_detail.html', context=context)





