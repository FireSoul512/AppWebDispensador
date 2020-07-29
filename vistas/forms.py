from django import forms
from .models import Fecha, Dispensar

class DateForm(forms.ModelForm):
    fecha = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    
    class Meta:
        model = Fecha
        fields = ['fecha']
    

class ListaHoras(forms.ModelForm):
    class Meta:
        model  = Dispensar
        fields = [
            'hora',
            'minuto',
            'id_usuario',
        ]
        labels = {
            'hora':'Hora',
            'minuto':'Minuto',
            'id_usuario':'Usuario',
        }
        widget = {
            'hora':forms.Select(attrs={'class':'form-control'}),
            'minuto':forms.Select(attrs={'class':'form-control'}),
            'id_usuario':forms.Select(attrs={'class':'form-control'}),
        }
