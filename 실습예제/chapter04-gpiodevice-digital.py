import machine
import utime

LEDR = machine.Pin(17, machine.Pin.OUT)

while True:
    LEDR.value(1)
    print( LEDR.value(  ) )
    utime.sleep_ms(2000)
    LEDR.value(0)
    print( LEDR.value(  ) )
    utime.sleep_ms(2000)
