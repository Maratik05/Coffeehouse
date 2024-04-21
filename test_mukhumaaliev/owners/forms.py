from django import forms
from owners.models import Owner


class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['username','last_name','email','password']

