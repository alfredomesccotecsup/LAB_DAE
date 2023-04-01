from django import forms

class CilindroForm(forms.Form):
    altura = forms.DecimalField(max_digits=10, decimal_places=2, label='Introduzca el diametro en metros')
    diametro = forms.DecimalField(max_digits=10, decimal_places=2, label='Introduzca la altura en metros')
