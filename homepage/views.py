from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from homepage import Cliente, Carro

# Create your views here.

def home(request):
    print('Página inicial')
    lista_carros = Carro.objects.all()
    template = loader.get_template("index.html")

    context = {
        'lista_carros': lista_carros,
    }

    return HttpResponse(template.render(context=context))
