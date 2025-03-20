from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Supply, Uniform
from .forms import SupplyForm, UniformForm

def supply_list(request):
    supplies = Supply.objects.all()
    return render(request, 'inventory_management/supply_list.html', {'supplies': supplies})

def supply_create(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supply_list')
    else:
        form = SupplyForm()
    return render(request, 'inventory_management/supply_form.html', {'form': form})

def supply_update(request, pk):
    supply = Supply.objects.get(pk=pk)
    if request.method == 'POST':
        form = SupplyForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('supply_list')
    else:
        form = SupplyForm(instance=supply)
    return render(request, 'inventory_management/supply_form.html', {'form': form})

def supply_delete(request, pk):
    supply = Supply.objects.get(pk=pk)
    if request.method == 'POST':
        supply.delete()
        return redirect('supply_list')
    return render(request, 'inventory_management/supply_confirm_delete.html', {'supply': supply})

def uniform_list(request):
    uniforms = Uniform.objects.all()
    return render(request, 'inventory_management/uniform_list.html', {'uniforms': uniforms})

def uniform_create(request):
    if request.method == 'POST':
        form = UniformForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uniform_list')
    else:
        form = UniformForm()
    return render(request, 'inventory_management/uniform_form.html', {'form': form})

def uniform_update(request, pk):
    uniform = Uniform.objects.get(pk=pk)
    if request.method == 'POST':
        form = UniformForm(request.POST, instance=uniform)
        if form.is_valid():
            form.save()
            return redirect('uniform_list')
    else:
        form = UniformForm(instance=uniform)
    return render(request, 'inventory_management/uniform_form.html', {'form': form})

def uniform_delete(request, pk):
    uniform = Uniform.objects.get(pk=pk)
    if request.method == 'POST':
        uniform.delete()
        return redirect('uniform_list')
    return render(request, 'inventory_management/uniform_confirm_delete.html', {'uniform': uniform})