import string
from django.shortcuts import render
from django.http import HttpResponse

def calcular(request):
    context = {
        'titulo' : 'Operaciones Aritmeticas'
    }
    return render(request, 'formulario.html', context)

def calculado(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operador = request.POST['operador']
    resultado = 0
    signo = ""

    if operador == 'suma':
        resultado = num1 + num2
        signo = "+"
    elif operador == "resta":
        resultado = num1 - num2
        signo = "-"
    elif operador == "multiplicacion":
        resultado = num1 * num2
        signo = "x"
    elif operador == "Seleccion Obligatorio":
        operador = "?"
        signo = "?"
    else:
        resultado = "nulo"
    context = {
        'num1': request.POST['num1'],
        'num2': request.POST['num2'],
        'operador' : operador,
        'respuesta' : resultado,
        'signo' : signo,
        'titulo' : 'Operaciones Aritmeticas'
    }
    return render(request, 'calculado.html', context)
