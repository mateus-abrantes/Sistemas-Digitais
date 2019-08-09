#BIBLIOTECA DE COMUNICACAO SERIAL ENTRE ARDUINO E PYTHON
import serial

#CONEXÃO UTILIZANDO A PORTA DO LINUX
circuito = serial.Serial("/dev/ttyACM0",9600,timeout=1)

def serial_ard_py():
    while True :
        #VALOR ENVIADO PELO ARDUINO REPRESENTANDO A DISTANCIA EM CM
        DISTANCIA = int(circuito.readline(10))
        print(DISTANCIA)

        #SE A DISTANCIA FOR MENOR QUE 30 CM ATIVA O ESTADO 1
        if DISTANCIA <= 30 :
            circuito.write(b'1')
        #SE NÃO ATIVA O ESTADO 0
        else :
            circuito.write(b'0')

serial_ard_py()

