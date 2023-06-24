from django.urls import path
from . import views


urlpatterns = [
    path('', views.pu_results, name='pu_results'),
    # path('getdata/',views.pu,name="getdata"),
    # Ajax
    path('ajax/get-wards/', views.pu_results, name='get_wards'),
	path('ajax/get-pus/', views.pu_results, name='get_pus'),
    path('ajax/get-pus/result/', views.pu_results, name='get_pus_result'),
    path('ajax/get-total-pu-by-lga/', views.lga_pu_results, name='lga_pu_results'),
	path('poll/add/', views.add_new_pu_result, name='add_new_poll'),
]