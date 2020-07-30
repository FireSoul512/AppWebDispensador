#!/usr/bin/env python3
import smtplib

remitente = 'pet.dispenser.2412@gmail.com'
contra = 'ContraFacil512'

class Correo:
    def cor(destinatario, peso):
        asunto = ''
        mensaje = ''

        if peso == -440:
            asunto = 'Error de conexion'
            mensaje = 'Le informamos que el servidor no ha podido conectarse al dispensador, es posible que este apagado o no cuente con conexion a internet'
        elif peso < 30:
            asunto = 'Poco alimento'
            mensaje = 'Le informamos que el dispensador se esta quedando sin alimento, en este momento la cantidad de alimento con la que cuenta es de: ' + str(peso) +'g'
        else:
            asunto = 'Confirmacion'
            mensaje = 'Le informamos que el dispensador ha servido los alimentos a su mascota, en este momento la cantidad de alimento con la que cuenta es de: ' + str(peso) +'g'
        try:
            mensaje = 'Subject: {}\n\n{}'.format(asunto, mensaje)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login( remitente , contra )
            server.sendmail( remitente , destinatario , mensaje )
            server.quit()
        except:
            print('Error, el correo es incorrecto')