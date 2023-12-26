from django.urls import path
from homepage import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cadastro

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ok', views.Ok, name='sucesso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)