from django.urls import path

from locomotiv import views

urlpatterns = [
    path('number/', views.VagonDataListView.as_view(), name='number'),
    # new app APIs
    path('calculation-resistance/', views.NewAppCalculatingResistanceAPIVIew.as_view(), name='calculation-resistance'),
    path('number/upload/', views.UploadVagonNumberDataView.as_view(), name='upload-data-file'),
]
