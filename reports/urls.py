# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate_energy_report/', views.generate_energy_report, name='generate_energy_report'),
    path('generate_consumption_graph/', views.generate_consumption_graph, name='generate_consumption_graph'),
    path('monthly_consumption/', views.monthly_consumption, name='monthly_consumption'),
    path('product_comparison/', views.product_comparison, name='product_comparison'),
    path('energy_efficiency/', views.energy_efficiency, name='energy_efficiency'),
]
