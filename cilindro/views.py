from django.shortcuts import render
from .forms import CilindroForm
from decimal import Decimal

def calcular_volumen_cilindro(request):
    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            diametro = form.cleaned_data['diametro']
            radio = diametro / 2
            volumen = Decimal(3.1416) * (radio ** 2) * altura
            return render(request, 'cilindro/resultado.html', {'volumen': volumen})
    else:
        form = CilindroForm()
    return render(request, 'cilindro/formulario.html', {'form': form})
