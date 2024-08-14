from django.shortcuts import render,redirect
from.models import Cliente
from.models import Producto
from .forms import ProductoModelForm

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'listar_clientes.html', {'clientes':clientes})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request,'listar_productos.html', {'productos':productos})

def inicio(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoModelForm
    return render(request, 'agregar_producto.html', {'form': form})
            



            

