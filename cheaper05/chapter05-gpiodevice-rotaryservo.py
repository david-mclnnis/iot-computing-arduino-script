import machine
import utime

servo=machine.Pin(33, machine.Pin.OUT)
rotory = machine.Pin(32, machine.Pin.IN)

while True :
    adc=machine.ADC(rotory)
    adc.atten(machine.ADC.WIDTH_12BIT)
    rottaryval=adc.read()
    print(rottaryval)

    pwm=machine.PWM(servo, freq=50)
    if rottaryval < 1000 :
        pwm.duty(10)
    elif rottaryval >= 1000 and rottaryval < 2000 :
        pwm.duty(40)
    elif rottaryval >= 2000 and rottaryval < 3000 :
        pwm.duty(70)
    elif rottaryval >= 3000 and rottaryval < 4000 :
        pwm.duty(100)
    elif rottaryval >= 4000 :
        pwm.duty(130)
    
    utime.sleep_ms(1000)
    pwm.deinit()
    utime.sleep_ms(20)
