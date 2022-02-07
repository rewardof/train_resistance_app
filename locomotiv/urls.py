from django.contrib import admin
from django.urls import path, include

from locomotiv import views
from .utils import vagon_data_excel


urlpatterns = [
    path('number/', views.VagonDataListView.as_view(), name='number'),
    path('locomotivs/', views.LocomotivListListView.as_view(), name='locomotiv-list'),
    path('result/<int:locomotiv_id>/', views.CalculateResultView.as_view(), name='calculate-result_view'),
    path('vagons-list/', views.VagonDataList.as_view(), name='vagons-list'),
    path('delete-vagons-data/', views.DeleteVagonsData.as_view(), name='delete-vagons-data'),
    path('export-vagons-data/', vagon_data_excel, name='export-vagons-data'),
    path('export-resistance-data/', views.ResistanceFileDownload.as_view(), name='export-resistance-data'),
]
