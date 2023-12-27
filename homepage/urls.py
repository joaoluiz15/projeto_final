from django.urls import path
from homepage import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cadastro

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ok', views.sucesso, name='sucesso'),
    path('carro_imagens', views.carro_imagens, name='carro_imagens'),
    path('estoque', views.estoque, name='estoque'),
    path('atualizar/<str:pk>/', views.atualizar, name="atualizar"),
    path('comprar', views.comprar, name='comprar'),
    path('cliente', views.cliente, name='cliente'),
]