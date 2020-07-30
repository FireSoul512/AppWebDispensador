from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib import messages
import socket,datetime
from .models import Dispensar

from .forms import DateForm, ListaHoras


class vistaConf(FormView):
    def getUrl():
        return '/configure/'
    def get(self, request, *arg, **kargs):
        form = DateForm(request.GET or None)
        context={
            'form': form
        }
        return render(request,'index/conf.html',context)
    
    def post(self, request, *arg, **kargs):
        form = DateForm(request.POST or None)

        if form.is_valid():
            
            #hora de la pagina
            valid = form.data['fecha']
            date  = valid[:-5]
            time  = valid[11:]
            day   = date[0:2]
            month = date[3:5]
            year  = date[6:10]
            hour  = time[0:2]
            min   = time[3:5]
            #hora del server
            valid = datetime.datetime.now().__str__()
            date2 = valid[0:10]
            time2 = valid[11:-10] 
            hour2  = time2[0:2]
            min2   = time2[3:5]
            year2  = date2[0:4]
            month2 = date2[5:7]
            day2   = date2[8:10]
            
            if( year >= year2):
                if(month >= month2):
                    if(day >= day2):
                        bdate = True
                    elif(month > month2 and day <= day2):
                        bdate = True
                    else:
                        bdate = False
                        raise ValueError('Una fecha valida podria ser mañana')
                else:
                    raise ValueError('ingrese una fecha valida')
            else:
                raise ValueError('Ingrese una fecha valida')

            if bdate:
                if(hour >= hour2):
                    if(min >= min2):
                        self.object = form.save(commit=False)
                        self.object.save()
                    else:
                        raise ValueError('ingrese una hora valida')
                else:
                    raise ValueError('Ingrese una hora valida')

            
        return redirect('/configure/')
    
class vistaClass(View):

    #template = 'index.html'

    def get(self, request, *arg, **kargs):
        return render(request,'index/index.html')
    
   
    def post(self, request, *arg, **kargs):
        #boton de despachar
        if 'btn1' in request.POST.keys():

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                
                mensaje = "SERVO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                peso = peso + 'g'
                s.close()
                messages.info(request, peso)

                return render(request,'index/index.html')
            except:
                    messages.info(request, 'Dispensador desconectado')
                    return render(request,'index/index.html')
        #boton peso
        if 'btn2' in request.POST.keys():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                mensaje = "PESO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                peso = peso + 'g'
                s.close()
                messages.info(request, peso)

                return render(request,'index/index.html')
            except:
                messages.info(request, 'Dispensador desconectado')
                return render(request,'index/index.html')

        if 'btn3' in request.POST.keys():
            return redirect('hora_list')

class nextClas(View):
    def get(self, request, *arg, **kargs):
        return render(request,'index/next.html')

def hora_list(request):
    horas = Dispensar.objects.all().order_by('id')
    contexto = {'hora':horas}
    return render(request, 'index/registro_horario.html', contexto)

def hora_create(request):
    if request.method == 'POST':
        form = ListaHoras(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hora_list')
    else:
        form = ListaHoras()

    context = {'form':form}
    return render(request, 'index/hora_form.html', context)

def hora_edit(request, id_hora):
    hora = Dispensar.objects.get(id=id_hora)
    if request.method == 'GET':
        form = ListaHoras(instance=hora)
    else:
        form = ListaHoras(request.POST, instance=hora)
        if form.is_valid():
            form.save()
            return redirect('hora_list')
    context = {'form':form}
    return render(request, 'index/hora_form.html', context)

def hora_delete(request, id_hora):
    hora = Dispensar.objects.get(id=id_hora)
    if request.method == 'POST':
        hora.delete()
        return redirect('hora_list')
    context = {'hora':hora}
    return render(request, 'index/hora_delete.html', context)