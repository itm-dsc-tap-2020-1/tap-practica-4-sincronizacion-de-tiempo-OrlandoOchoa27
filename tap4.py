import datetime
from time import ctime
import ntplib
import os


sdt="time-e-g.nist.gov"



x=datetime.datetime.now()
print("Fecha y hora de inicio de peticion = %s" % x) 

print("\nObteniendo la hora del servidor NTP:")
cntp= ntplib.NTPClient()
respuesta=cntp.request(sdt)
ha=datetime.datetime.strptime(ctime(respuesta.tx_time),"%a %b %d %H:%M:%S %Y")
print("Hora de llegada de " + sdt + ": " + str(ha) + "\n")

ajuste=(ha-x)/2
print("Ajuste: "+str(ajuste)+"\n")

reloj=x+ajuste


print("\nAjustando Tiempo:")
# call("date -u \"" + fecha_hora.strftime("%d %b %Y %H:%M:%S") + "\"",shell = True)
# call("hwclock --systohc",shell = True)
os.system(reloj)