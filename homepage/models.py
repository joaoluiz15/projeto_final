from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True, default=0)
    nome = models.CharField(max_length=50)

class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    ano_fabricacao = models.IntegerField()
    preco = models.FloatField(default=0, null=True, blank=True)
    categoria = models.CharField(max_length=10)
    cpf_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
