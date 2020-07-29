from django.contrib.auth.models import User
from django import forms

ERROR_MESSAGE_USER={'unique':'El username ya esta en uso','invalid':'usuario o contraseña incorrectos'}
ERROR_MESSAGE_PASSWORD={'required':'El password es requerido'}
ERROR_MESSAGE_EMAIL={'invalid':'Formato no valido, pruebe otra vez'}

class RegisterBussinessForm(forms.ModelForm):
    first_name = forms.CharField(label='',required=True)
    last_name = forms.CharField(label='',required=True)
    password = forms.CharField(max_length=20, required=True,widget=forms.PasswordInput(),error_messages=ERROR_MESSAGE_PASSWORD)
    email = forms.CharField(required=True, error_messages=ERROR_MESSAGE_EMAIL)
    
    def __init__(self,*args,**kargs):
        super(RegisterBussinessForm,self).__init__(*args,**kargs)
        self.fields['username'].widget.attrs.update({'id':'userR','class':'form-control','placeholder':'Usuario'})
        self.fields['first_name'].widget.attrs.update({'id':'first_nameR','class':'form-control','placeholder':'Nombre'})
        self.fields['last_name'].widget.attrs.update({'id':'last_nameR','class':'form-control','placeholder':'Apellidos'})
        self.fields['password'].widget.attrs.update({'id':'passwordR','class':'form-control','placeholder':'Password'})
        self.fields['email'].widget.attrs.update({'id':'emailR','class':'form-control','placeholder':'Email'})
    
    class Meta():
        model = User
        fields=['username','password','first_name','last_name','email']