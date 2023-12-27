from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from homepage.models import Cliente, Carro
from .forms import CarroForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    print('Página inicial')
    lista_carros = Carro.objects.all()
    qnt_carros_disp = Carro.objects.all().count()
    template = loader.get_template("index.html")

    context = {
        'lista_carros': lista_carros,
        'qnt_carros_disp': qnt_carros_disp,
    }

    return HttpResponse(template.render(context=context))

def cadastro(request):
    print('Cadastrar carros recém-chegados')
    template = loader.get_template("cadastro.html")
    
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            sucesso = 'Cadastrado'
            return render(request, 'cadastro.html', {'form': form, 'sucesso': sucesso})
        
    else:
        form = CarroForm()
        
    return render(request, 'cadastro.html', {'form': form})

def sucesso(request):
    return HttpResponse('Cadastrado. Clique aqui para retornar à página inicial.')

def carro_imagens(request):
    if request.method == 'GET':
        Carros = Carro.objects.all()
        return render((request, 'carro_imagens.html', {'carro_imagens: Carros'}))


def estoque(request):
    return render(request, 'estoque.html')


def atualizar(request, pk):
	queryset = Carro.objects.get(id=pk)
	form = CarroUpdate(instance=queryset)
	if request.method == 'POST':
		form = CarroUpdate(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return render(request, 'atualizar.html', context)

	context = {
		'form':form
	}
	return render(request, 'atualizar.html', context)



def comprar(request):
     return render(request, 'comprar.html')

def cliente(request):
     return render(request, 'cliente.html')