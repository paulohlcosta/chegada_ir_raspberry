import RPi.GPIO as GPIO #VAMOS USAR SOMENTE O RECEPTOR (NAO O EMISSOR)
import time
b=repetir=0
interrompeu=time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

GPIO.output(27,1)
print(buscando sinal infravermelho)

while True
    i=GPIO.input(17)
    if i==1 and b==0
        interrompeu=time.time()
        b=1  #ALTERNANCIA
    if i==0 and b==1  #QUANDO HÁ RECEPÇÃO DO SINAL
        repetir=1
        b=0  #ALTERNANCIA
    if i==1 and repetir==1 and time.time()(interrompeu+0.07)
        #print(time.time()-interrompeu)
        GPIO.output(27,0)
        time.sleep(3)
        GPIO.output(27,1)
        time.sleep(0.1)
        repetir=0  #PARA NAO REPETIR A INDICAÇÃO
    #time.sleep(0.01)    
GPIO.cleanup()

