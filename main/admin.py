from django.contrib import admin
from .models import EnergyProduct, EnergyConsumption, Consumer

# Customize the admin display for EnergyProduct
class EnergyProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

# Customize the admin display for EnergyConsumption
class EnergyConsumptionAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'product', 'consumption_date', 'units_consumed')
    list_filter = ('product', 'consumption_date')
    search_fields = ('consumer__name', 'product__name', 'consumption_date')
    date_hierarchy = 'consumption_date'

# Customize the admin display for Consumer
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email')
    search_fields = ('name', 'contact_email')

# Register the customized admin classes for your models
admin.site.register(EnergyProduct, EnergyProductAdmin)
admin.site.register(EnergyConsumption, EnergyConsumptionAdmin)
admin.site.register(Consumer, ConsumerAdmin)
