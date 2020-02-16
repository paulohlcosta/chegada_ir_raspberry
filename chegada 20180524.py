import RPi.GPIO as GPIO   
import time
GPIO.setmode(GPIO.BCM)

class Sensor:

    def __init__(self, id, light):
        self.id = id
        self.light = light
        self.old = False
        self.off_time = time.time()
        self.sinalizar = False
        GPIO.setup(id,GPIO.IN)
        GPIO.setup(light,GPIO.OUT)

    def alternated(self, agora, old): #vai retornar informando se houve alternancia
        self.value = GPIO.input(self.id)       
        if self.value == self.old:    #NAO HOUVE ALTERNANCIA
            pass                        
        elif self.value and self.old == False:#    ALTERNOU PARA INTERROMPIDO
            self.off_time = agora
            self.old = True
        elif self.value == False and self.old:#      ALTERNOU PARA RECEBIDO
            #print self.light, self.value, '{:.2f}'.format(agora-self.off_time), 'alternou para recebendo'
            self.old = False
            self.sinalizar = True

        if self.value and (agora > (self.off_time+0.07)) and self.sinalizar:
            s1.sinalizar = s2.sinalizar = False
            self.won()
            #print 'rodando...'

    def won(self):
        #print self.light, 'off_time:', '{:.2f}'.format(agora-s1.off_time), 'pausa 5 segundos.'
        self.sinalizar = False
        GPIO.output(self.light,True)
        time.sleep(0.2)
        GPIO.output(self.light,False)
        time.sleep(0.2)
        GPIO.output(self.light,True)
        time.sleep(0.2)
        GPIO.output(self.light,False)
        time.sleep(0.2)
        GPIO.output(self.light,True)
        time.sleep(0.2)
        GPIO.output(self.light,False)
        time.sleep(0.2)
        GPIO.output(self.light,True)
        time.sleep(0.2)
        GPIO.output(self.light,False)
        time.sleep(0.2)
        GPIO.output(self.light,True)
        time.sleep(1)
        GPIO.output(self.light,False)
        time.sleep(1)
        GPIO.output(self.light,True)
        time.sleep(1)
        GPIO.output(self.light,False)
        time.sleep(1)
        GPIO.output(self.light,True)
        time.sleep(1)
        GPIO.output(self.light,False)
        time.sleep(1)
        GPIO.output(self.light,True)
        time.sleep(1)

        GPIO.output(self.light,False)
        time.sleep(1)



if __name__ == '__main__':
    s1 = Sensor(17, 18)
    s2 = Sensor(4, 27)
	
    print ("Vamos comecar acendendo as luzes")
    GPIO.output(s1.light,False)
    GPIO.output(s2.light,True)
    time.sleep(0.2)
    GPIO.output(s1.light,True)
    GPIO.output(s2.light,False)
    time.sleep(0.2)
    GPIO.output(s1.light,False)
    GPIO.output(s2.light,True)
    time.sleep(0.2)
    GPIO.output(s1.light,True)
    GPIO.output(s2.light,False)
    time.sleep(0.2)
    GPIO.output(s1.light,False)
    GPIO.output(s2.light,True)
    time.sleep(0.2)
    GPIO.output(s1.light,True)
    GPIO.output(s2.light,False)
    time.sleep(0.2)
    GPIO.output(s1.light,False)
    GPIO.output(s2.light,True)
    time.sleep(0.2)
    GPIO.output(s1.light,True)
    GPIO.output(s2.light,False)
    time.sleep(0.2)    
    GPIO.output(s1.light,False)
    GPIO.output(s2.light,False)
    print ("Aguardando sinal infravermelho")
	
    while True:
		
		

        agora = time.time()

        r1 = s1.alternated(agora, s1.old)
        
        agora = time.time()
        
        r2 = s2.alternated(agora, s2.old)
 
