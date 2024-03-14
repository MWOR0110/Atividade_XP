from django.contrib import admin
from django.urls import path, include
from meu_app.views import exibir_dados, receber_dados  # Importe ambas as visualizações

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', exibir_dados),  # Rota vazia redirecionando para a visualização exibir_dados
    path('meu_app/', include('meu_app.urls')),  # Inclua as URLs do aplicativo meu_app
]
