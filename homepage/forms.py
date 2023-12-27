
from django import forms
from .models import Carro, Cliente

#form de inserção
class CarroForm(forms.ModelForm):

	class Meta:
		model = Carro
		fields = ['nome', 'ano_fabricacao', 'categoria', 'preco', 'imagem', 'cpf_cliente']


#form de update
class CarroUpdate(forms.ModelForm):

	class Meta:
		model = Carro
		fields = ['nome', 'ano_fabricacao', 'categoria', 'preco', 'imagem']
  
#form cadastro cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ['cpf', 'nome']
  