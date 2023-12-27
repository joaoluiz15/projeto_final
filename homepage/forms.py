
from django import forms
from .models import Carro

#form de inserção
class CarroForm(forms.ModelForm):

	class Meta:
		model = Carro
		fields = ['nome', 'ano_fabricacao', 'categoria', 'imagem']


#form de update
class CarroUpdate(forms.ModelForm):

	class Meta:
		model = Carro
		fields = ['nome', 'ano_fabricacao', 'categoria', 'imagem']