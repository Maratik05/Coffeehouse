from django.urls import path
from .views import AddOwnerView,CoffeHouseOwner, EditDeleteOwner

urlpatterns = [
    path('add/', AddOwnerView.as_view()),
    path('<int:owner_id>/', CoffeHouseOwner.as_view(),name='ownersprofile'),
    path('<int:owner_id>/edit', EditDeleteOwner.as_view())
]