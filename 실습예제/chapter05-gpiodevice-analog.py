import machine
import utime


while True :
    print("hello")
    buzz=machine.Pin(25, machine.Pin.OUT)
    pwm=machine.PWM(buzz)

    pwm.freq(1000)
    pwm.duty(1023)
    utime.sleep_ms(500)

    pwm.freq(1000)
    pwm.duty(512)
    utime.sleep_ms(500)

    pwm.freq(2000)
    pwm.duty(300)
    utime.sleep_ms(500)

    pwm.freq(3000)
    pwm.duty(100)
    utime.sleep_ms(500)

    pwm.deinit()
