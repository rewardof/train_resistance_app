from django.contrib import admin
from django.urls import path, include

from locomotiv import views
from .utils import vagon_data_excel


urlpatterns = [
    path('number/', views.VagonDataListView.as_view(), name='number'),
    path('locomotivs/', views.LocomotivListListView.as_view(), name='locomotiv-list'),
    path('result/', views.CalculateResultView.as_view(), name='calculate-result'),
    path('vagons-list/', views.VagonDataList.as_view(), name='vagons-list'),
    path('delete-vagons-data/', views.DeleteVagonsData.as_view(), name='delete-vagons-data'),
    path('export-vagons-data/', vagon_data_excel, name='export-vagons-data'),
    # path('export-resistance-data/', views.resistance_export_excel, name='export-resistance-data'),
    path('switch-list/', views.RailRoadSwitchList.as_view(), name='switch-list'),
    path('finding_distance/', views.TrainRunningDistance.as_view(), name='finding-distance'),
    path('railway-charachteristics-list/', views.RailRoadCharacteristicLIstView.as_view(), name='railway-charachteristics-list'),
    # new app APIs
    path('calculation-resistance/', views.NewAppCalculatingResistanceAPIVIew.as_view(), name='calculation-resistance'),
    path('number/upload/', views.UploadVagonNumberDataView.as_view(), name='upload-data-file'),
]
