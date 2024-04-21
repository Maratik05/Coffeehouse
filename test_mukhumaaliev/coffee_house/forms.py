from django import forms
from coffee_house.models import CoffeeHouse


class AddCoffeHouseForm(forms.ModelForm):
    class Meta:
        model = CoffeeHouse
        fields = ['title', 'schedule','owner','description']