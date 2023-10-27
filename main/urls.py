from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Energy Product URLs
    path('energy_products/create/', views.create_energy_product, name='create_energy_product'),
    path('energy_products/', views.list_energy_products, name='list_energy_products'),
    path('energy_products/<int:pk>/edit/', views.edit_energy_product, name='edit_energy_product'),
    path('energy_products/<int:pk>/delete/', views.delete_energy_product, name='delete_energy_product'),

    # Energy Consumption URLs
    path('energy_consumptions/create/', views.create_energy_consumption, name='create_energy_consumption'),
    path('energy_consumptions/', views.list_energy_consumptions, name='list_energy_consumptions'),
    path('energy_consumptions/<int:pk>/edit/', views.edit_energy_consumption, name='edit_energy_consumption'),
    path('energy_consumptions/<int:pk>/delete/', views.delete_energy_consumption, name='delete_energy_consumption'),

    # Consumer URLs
    path('consumers/create/', views.create_consumer, name='create_consumer'),
    path('consumers/', views.list_consumers, name='list_consumers'),
    path('consumers/<int:pk>/edit/', views.edit_consumer, name='edit_consumer'),
    path('consumers/<int:pk>/delete/', views.delete_consumer, name='delete_consumer'),
]
