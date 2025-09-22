# clientes/views.py

from django.http import JsonResponse

def lista_clientes(request):
    dados_clientes = [
        {"id": 1, "nome": "Maria Silva", "email": "maria.silva@example.com"},
        {"id": 2, "nome": "João Pereira", "email": "joao.p@example.com"},
        {"id": 3, "nome": "Ana Costa", "email": "ana.costa@example.com"},
    ]
    

    return JsonResponse({"clientes": dados_clientes})