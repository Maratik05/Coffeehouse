from django.urls import path
from coffee_house.views import get_owner
from .views import AddOwnerView, EditDeleteOwner
urlpatterns = [
    path('add/', AddOwnerView.as_view()),
    path('<int:owner_id>/', get_owner,name='ownersprofile'),
    path('<int:owner_id>/edit', EditDeleteOwner.as_view(), name='ownereditdelete')
]