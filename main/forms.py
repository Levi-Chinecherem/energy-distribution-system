# main/forms.py

from django import forms
from .models import EnergyProduct, EnergyConsumption, Consumer

class EnergyProductForm(forms.ModelForm):
    class Meta:
        model = EnergyProduct
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EnergyConsumptionForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumption
        fields = ['consumer', 'product', 'consumption_date', 'units_consumed']
        widgets = {
            'consumer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'consumption_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'units_consumed': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'contact_email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
