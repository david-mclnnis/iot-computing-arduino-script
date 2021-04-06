from machine import UART
import utime

uart=UART(1,115200)
uart.init(115200,bits=8,parity=None,stop=1,rx=12,tx=14)
while True:

    ch = uart.read()

    if ch == b'g' and ch != b'' :
        print("g command execute")
        uart.write("executed g command\n")
    elif ch == b'f' and ch != b'' :
        print("f command execute")
        uart.write("executed f command\n")
    utime.sleep_ms(100)

from machine import UART
import utime

uart=UART(1,115200)
uart.init(115200,bits=8,parity=None,stop=1,rx=12,tx=14)
while True:

    ch = uart.read()

    if ch == b'g' and ch != b'' :
        print("g command execute")
        uart.write("executed g command\n")
    elif ch == b'f' and ch != b'' :
        print("f command execute")
        uart.write("executed f command\n")
    utime.sleep_ms(100)
