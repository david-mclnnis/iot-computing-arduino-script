import machine
import utime

LEDR = machine.Pin(17, machine.Pin.OUT)
LEDG = machine.Pin(16, machine.Pin.OUT)
LEDB = machine.Pin(27, machine.Pin.OUT)

while True:
  LEDR.value(1)
  utime.sleep_ms(20)
  LEDR.value(0)
  
  LEDG.value(1)
  utime.sleep_ms(20)
  LEDG.value(0)
  
  LEDG.value(1)
  utime.sleep_ms(20)
  LEDG.value(0)
