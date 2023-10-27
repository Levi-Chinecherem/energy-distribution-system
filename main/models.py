# main/models.py

from django.db import models

class EnergyProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class EnergyConsumption(models.Model):
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)
    product = models.ForeignKey(EnergyProduct, on_delete=models.CASCADE)
    consumption_date = models.DateField()
    units_consumed = models.FloatField()

    def __str__(self):
        return self.consumer
    
class Consumer(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
    