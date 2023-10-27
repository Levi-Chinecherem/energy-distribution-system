# reports/views.py
from django.shortcuts import render
import matplotlib.pyplot as plt
from main.models import EnergyConsumption, EnergyProduct
import pandas as pd
from django.db.models import Sum
from calendar import month_name
import os
from django.db.models.functions import TruncMonth

# Directory for energy report chart
report_directory = 'static/reports'
os.makedirs(report_directory, exist_ok=True)

def generate_energy_report(request):
    # Retrieve data from the EnergyConsumption model
    consumption_data = EnergyConsumption.objects.all()

    # Example: Calculate total consumption per product
    product_data = EnergyProduct.objects.all()
    consumption_by_product = {}
    for product in product_data:
        product_consumption = consumption_data.filter(product=product)
        total_consumption = sum([entry.units_consumed for entry in product_consumption])
        consumption_by_product[product.name] = total_consumption

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(consumption_by_product.keys(), consumption_by_product.values())
    plt.xlabel('Energy Product')
    plt.ylabel('Total Consumption')
    plt.title('Energy Consumption by Product')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the chart to a file
    chart_file = 'static/reports/energy_report.png'
    plt.savefig('static/reports/energy_report.png')
    plt.close()

    # Check if the chart file exists
    if os.path.exists(chart_file):
        return render(request, 'reports/energy_report.html', {'chart_file': chart_file})
    else:
        return render(request, 'reports/energy_report_no_file.html')

def generate_consumption_graph(request):
    # Retrieve data from the EnergyConsumption model
    consumption_data = EnergyConsumption.objects.all()

    # Example: Create a time series line chart
    consumption_df = pd.DataFrame(list(consumption_data.values('consumption_date', 'units_consumed')))
    consumption_df['consumption_date'] = pd.to_datetime(consumption_df['consumption_date'])
    
    plt.figure(figsize=(12, 6))
    plt.plot(consumption_df['consumption_date'], consumption_df['units_consumed'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Units Consumed')
    plt.title('Energy Consumption Over Time')
    plt.grid(True)
    
    # Save the chart to a file
    chart_file = 'static/reports/consumption_graph.png'
    plt.savefig('static/reports/consumption_graph.png')
    plt.close()

    # Check if the chart file exists
    if os.path.exists(chart_file):
        return render(request, 'reports/consumption_graph.html', {'chart_file': chart_file})
    else:
        return render(request, 'reports/consumption_graph.html')
    
def monthly_consumption(request):
    # Retrieve data from the EnergyConsumption model
    consumption_data = EnergyConsumption.objects.annotate(
        month=TruncMonth('consumption_date')
    ).values('month').annotate(total_consumption=Sum('units_consumed'))

    # Create a line chart for monthly consumption
    labels = [month['month'].strftime('%B %Y') for month in consumption_data]
    data = [month['total_consumption'] for month in consumption_data]

    return render(request, 'reports/monthly_consumption.html', {'labels': labels, 'data': data})

def product_comparison(request):
    product_data = EnergyProduct.objects.all()
    product_consumption = {}
    
    for product in product_data:
        product_consumption[product.name] = EnergyConsumption.objects.filter(product=product).aggregate(total_consumption=Sum('units_consumed'))

    # Sort products by consumption
    sorted_products = sorted(product_consumption.items(), key=lambda x: x[1]['total_consumption'], reverse=True)

    return render(request, 'reports/product_comparison.html', {'sorted_products': sorted_products})

# Utility function to get month name
def get_month_name(month):
    return month_name[month]

def energy_efficiency(request):
    # Calculate energy efficiency of each product
    product_data = EnergyProduct.objects.all()
    efficiency_data = []

    for product in product_data:
        efficiency = calculate_efficiency(product)
        efficiency_data.append({'product': product, 'efficiency': efficiency})

    return render(request, 'reports/energy_efficiency.html', {'efficiency_data': efficiency_data})

# Utility function to calculate energy efficiency
def calculate_efficiency(product):
    # Get all consumption entries for the given product
    consumptions = EnergyConsumption.objects.filter(product=product)

    # Calculate total energy consumed
    total_energy_consumed = sum(consumption.units_consumed for consumption in consumptions)

    # Your logic for calculating energy efficiency based on the above data
    # For this case, let's assume efficiency is the total energy consumed
    # divided by the number of consumption entries.
    if consumptions.count() > 0:
        efficiency_value = total_energy_consumed / consumptions.count()
    else:
        efficiency_value = 0  # Handle the case when there are no consumption entries.

    return efficiency_value
