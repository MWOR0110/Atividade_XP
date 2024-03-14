from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Dados

def receber_dados(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dados = Dados.objects.create(
            sensor=data.get('Sensor'),
            botao=data.get('Botao'),
            liga_robo=data.get('LigaRobo'),
            reset_contador=data.get('ResetContador'),
            valor_contagem=data.get('Valor Contagem')
        )
        return JsonResponse({'message': 'Dados recebidos com sucesso!'})
    else:
        return JsonResponse({'error': 'Método não permitido!'}, status=405)

def exibir_dados(request):
    dados = Dados.objects.last()  # Busca o último objeto Dados no banco de dados
    return render(request, 'template.html', {'dados': dados})

