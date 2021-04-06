import machine
import utime

swit=machine.Pin(32, machine.Pin.IN)
buzz=machine.Pin(33, machine.Pin.OUT)

while True :
    print("swit="+str(swit.value(  )))
    print("buzz="+str(buzz.value(  )))
    if swit.value()==0 :
        buzz.value(1)
    else :
        buzz.value(0)
    utime.sleep_ms(20)
