from django.shortcuts import render, redirect
from .forms import Sorveteforms
from .models import Sorvete

def sorvete_pedido(request):
    if request.method == 'POST':
        form = Sorveteforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')# redireciona para a pagina de sucesso após salvar
    else:
        form = Sorveteforms()
    return render(request, 'main/index.html', {'form':form})

def pedidos(request):
    query = Sorvete.objects.all()
    return render (request, 'main/lista.html', {'query': query})