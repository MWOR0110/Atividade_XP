from django.urls import path
from .views import receber_dados, exibir_dados

urlpatterns = [
    path('receber/', receber_dados, name='receber_dados'),  # Rota para receber os dados
    path('exibir/', exibir_dados, name='exibir_dados'),
]
