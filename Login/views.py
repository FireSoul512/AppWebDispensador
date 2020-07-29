from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.views.generic.edit import FormView


class LoginClass(View):
    templates = 'login.html'
    
    message = ""
    
    def get(self, request, *arg, **kargs):
        if request.user.is_authenticated:
            next_url =request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/index/')
        return render(request,self.templates,{})
    
    def post(self, request, *arg, **kargs):
        user_post = request.POST['user']
        passw_post = request.POST['pass']
        user_session = authenticate(username = user_post, password = passw_post)
        #validacion
        if user_session is not None:
            login_django(request, user_session) 
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/index/')
        else:
            self.message = 'Usuario o contraseña incorrecto'
            return render(request, self.templates, self.get_contex())
    def get_contex(self):
        return {
            'error':self.message,
        } 


class l(View):
    def get(self, request, *arg, **kargs):
        print("l line 50")
        logout(request)
        return redirect('login')

        
