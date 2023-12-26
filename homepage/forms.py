
from django import forms
from .models import Carro


class CarroForm(forms.ModelForm):

	class Meta:
		model = Carro
		fields = ['nome', 'ano_fabricacao', 'categoria', 'imagem']
