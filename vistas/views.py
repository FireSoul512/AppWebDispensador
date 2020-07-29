from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib import messages
import socket,datetime

from .forms import DateForm


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

        print('form',form.data['fecha'])
        
        print(form)
        print(form.is_valid())
        print(form.is_valid)

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
            print(hour,':',min)
            print('select: ',valid)
            #hora del server
            valid = datetime.datetime.now().__str__()
            print(valid)
            date2 = valid[0:10]
            time2 = valid[11:-10] 
            hour2  = time2[0:2]
            min2   = time2[3:5]
            year2  = date2[0:4]
            month2 = date2[5:7]
            day2   = date2[8:10]
            print(hour2,':',min2)
            
            if( year >= year2):
                if(month >= month2):
                    if(day >= day2):
                        bdate = True
                    elif(month > month2 and day <= day2):
                        print(date,':',day2,'/',month2,'/',year2)
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
                print("boton despachar")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                
                mensaje = "SERVO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                print("El peso actual de del dispensador es de: ",msg.decode("utf-8"),"g")
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                s.close()
                print()
                print("ADIOS")
                messages.info(request, peso)

                return render(request,'index/index.html')
            except:
                    messages.info(request, 'Error')
                    print("No se pudo establecer conexion ;v")
                    return render(request,'index/index.html')
        #boton peso
        if 'btn2' in request.POST.keys():
            try:
                print("boton peso")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                mensaje = "SERVO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                print("El peso actual del dispensador es de: ",msg.decode("utf-8"),"g")
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                s.close()
                print()
                print("ADIOS")
                messages.info(request, peso)

                return render(request,'index/index.html')

            except:
                messages.info(request, 'Error')
                print("No se pudo establecer conexion ;v")
                return render(request,'index/index.html')
        if 'btn3' in request.POST.keys():
            
            r = vistaConf.getUrl()

            return redirect(r)

class nextClas(View):
    def get(self, request, *arg, **kargs):
        return render(request,'index/next.html')