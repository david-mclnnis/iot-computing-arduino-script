'''
    I2C LCD1602 demo
    Author: shaoziyang
    Date:   2018.2
    http://www.micropython.org.cn
'''
from machine import I2C, Pin
from cheaper06-lib-i2clcd import LCD1602
from time import sleep_ms

i2c = I2C(0, sda=Pin(21), scl=Pin(22))

LCD = LCD1602(i2c)
LCD.puts("I2C LCD1602")
n = 0
while 1:
    LCD.puts(n, 0, 1)
    n += 1
    sleep_ms(1000)
