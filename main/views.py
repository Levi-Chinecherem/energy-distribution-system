# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import EnergyProduct, EnergyConsumption, Consumer
from .forms import EnergyProductForm, EnergyConsumptionForm, ConsumerForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def create_energy_product(request):
    if request.method == 'POST':
        form = EnergyProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_energy_products')
    else:
        form = EnergyProductForm()
    return render(request, 'main/create_energy_product.html', {'form': form})

@login_required
def list_energy_products(request):
    products = EnergyProduct.objects.all()
    return render(request, 'main/list_energy_products.html', {'products': products})

@login_required
def edit_energy_product(request, pk):
    product = get_object_or_404(EnergyProduct, pk=pk)
    if request.method == 'POST':
        form = EnergyProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_energy_products')
    else:
        form = EnergyProductForm(instance=product)
    return render(request, 'main/edit_energy_product.html', {'form': form})

@login_required
def delete_energy_product(request, pk):
    product = get_object_or_404(EnergyProduct, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_energy_products')
    return render(request, 'main/delete_energy_product.html', {'product': product})


@login_required
def create_energy_consumption(request):
    if request.method == 'POST':
        form = EnergyConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_energy_consumptions')
    else:
        form = EnergyConsumptionForm()
    return render(request, 'main/create_energy_consumption.html', {'form': form})

@login_required
def list_energy_consumptions(request):
    consumptions = EnergyConsumption.objects.all()
    return render(request, 'main/list_energy_consumptions.html', {'consumptions': consumptions})

@login_required
def edit_energy_consumption(request, pk):
    consumption = get_object_or_404(EnergyConsumption, pk=pk)
    if request.method == 'POST':
        form = EnergyConsumptionForm(request.POST, instance=consumption)
        if form.is_valid():
            form.save()
            return redirect('list_energy_consumptions')
    else:
        form = EnergyConsumptionForm(instance=consumption)
    return render(request, 'main/edit_energy_consumption.html', {'form': form})

@login_required
def delete_energy_consumption(request, pk):
    consumption = get_object_or_404(EnergyConsumption, pk=pk)
    if request.method == 'POST':
        consumption.delete()
        return redirect('list_energy_consumptions')
    return render(request, 'main/delete_energy_consumption.html', {'consumption': consumption})


@login_required
def create_consumer(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_consumers')
    else:
        form = ConsumerForm()
    return render(request, 'main/create_consumer.html', {'form': form})

@login_required
def list_consumers(request):
    consumers = Consumer.objects.all()
    return render(request, 'main/list_consumers.html', {'consumers': consumers})

@login_required
def edit_consumer(request, pk):
    consumer = get_object_or_404(Consumer, pk=pk)
    if request.method == 'POST':
        form = ConsumerForm(request.POST, instance=consumer)
        if form.is_valid():
            form.save()
            return redirect('list_consumers')
    else:
        form = ConsumerForm(instance=consumer)
    return render(request, 'main/edit_consumer.html', {'form': form})

@login_required
def delete_consumer(request, pk):
    consumer = get_object_or_404(Consumer, pk=pk)
    if request.method == 'POST':
        consumer.delete()
        return redirect('list_consumers')
    return render(request, 'main/delete_consumer.html', {'consumer': consumer})
