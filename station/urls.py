from django.urls import path

from station import views

urlpatterns = [
    path(
        'process-natural-list/',
        views.ProcessNaturalList.as_view(),
        name='process-natural-list'
    ),
]
