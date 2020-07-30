#!/usr/bin/env python3
import socket
from correos import Correo

class Despachar:
    def inicio(destinatario):
        iprasp = '192.168.1.71'#Cambiar al subir el proyecto
        msg = '-440'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect( (iprasp,7080) )
            mensaje = 'SERVO'
            s.send(bytes(mensaje, "utf-8"))
            msg = s.recv(1024)
            s.close()
        except:
            msg = '-440'

        recibido = int(msg)

        Correo.cor(destinatario, recibido)