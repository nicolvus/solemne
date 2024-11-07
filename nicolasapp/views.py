from django.shortcuts import render
from .models import Platos, Categoria

def index(request):
    if request.method == 'POST':
        nuevo_plato = request.POST.get('item')
        precio = request.POST.get('precio')
        ingredientes = request.POST.get('ingredientes')
        categoria_id = request.POST.get('categoria')
        if nuevo_plato and precio and ingredientes and categoria_id:
            categoria = Categoria.objects.get(id=categoria_id)
            Platos.objects.create(
                nombre_plato=nuevo_plato,
                precio=precio,
                ingredientes=ingredientes,
                categoria=categoria
            )

    platos = Platos.objects.all()
    categorias = Categoria.objects.all()
    context = {'platos': platos, 'categorias': categorias}
    return render(request, 'index.html', context)

def submit():
    