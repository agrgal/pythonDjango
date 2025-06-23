from django.shortcuts import render
from .models import Cliente, Empleados
from django.http import HttpResponse
# Create your views here.

def misClientes(request):
    objeto = Cliente.objects.all().values('nombre')  # Obtiene todos los objetos de la tabla Cliente
    print(objeto)  # Imprime los objetos obtenidos en la consola del servidor
    response_var="<h1>Hola</h1>"  # Variable para almacenar la respuesta HTML
    for cada in objeto:
        response_var += f'<h2>Cliente{cada}</h2><br>'
    return HttpResponse(response_var)  # Devuelve el nombre del cliente