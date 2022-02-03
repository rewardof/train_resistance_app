from django.contrib import admin
from django.urls import path, include

from locomotiv import views

urlpatterns = [
    path('number/', views.VagonDataListView.as_view(), name='number'),
    path('locomotivs/', views.LocomotivListListView.as_view(), name='locomotiv-list')

]