from django.contrib import admin
from django.urls import path, include # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui todas as URLs do arquivo 'clientes/urls.py'
    # Qualquer acesso a 'api/' será redirecionado para o nosso app de clientes
    path('api/', include('clientes.urls')), 
]