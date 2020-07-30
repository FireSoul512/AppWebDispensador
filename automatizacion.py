from datetime import datetime
import time
import smtplib
import sqlite3
from despachar import Despachar

base_datos = '/home/jorgeliy/Web/AppWebDispensador/db.sqlite3'

def ciclo():
    romper = False
    while True:
        now = datetime.now()
        hora = now.hour
        minuto = now.minute
        try:
            con = sqlite3.connect(base_datos)
            cursorObj = con.cursor()
            cursorObj.execute('SELECT vistas_dispensar.hora, vistas_dispensar.minuto, auth_user.email FROM vistas_dispensar, auth_user WHERE vistas_dispensar.id_usuario_id = auth_user.id')
            rows = cursorObj.fetchall()
            for row in rows:
                if row[0] == hora and row[1] == minuto:
                    Despachar.inicio(row[2])
                    romper = True
                    break
            if romper:
                break
        except:
            print('Error')
        time.sleep(60)

def sincronizar_horario():
    time.sleep(1)
    now = datetime.now()
    hora = now.hour
    minuto = now.minute
    if hora == 23 and  minuto == 59:
        hora = 0
        minuto = 0
    elif minuto == 59:
        hora = hora + 1
        minuto = 0
    else:
        minuto = minuto + 1

    while True:
        if  now.hour == hora and now.minute == minuto:
            break
        now = datetime.now()

while True:
    sincronizar_horario()
    ciclo()