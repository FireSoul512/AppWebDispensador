from django import forms
from .models import Fecha

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
    