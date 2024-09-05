from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('all_members/', views.all_members, name='all_members'),
    path('all_members/details/<int:id>', views.details, name='details'),
]