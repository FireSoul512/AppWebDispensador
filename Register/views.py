from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from Register.forms import RegisterBussinessForm

# Create your views here.
class RegisterClass(FormView):
    templates = 'Register/Register.html'
    
    def get(self,request,*args,**kargs):
        form = RegisterBussinessForm(request.GET or None)
        context={
            'form': form
        }
        return render(request, self.templates,context)
    
    def post(self,request,*args,**kargs):
        form = RegisterBussinessForm(request.POST or None)
        print(form.data)
        print(form.is_valid())
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.set_password(self.object.password)
            self.object.save()
        return redirect('login')