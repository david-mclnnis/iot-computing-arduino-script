import machine
import cheaper06-lib-spidotmatrix

hspi = machine.SPI(1, 10000000, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))
ss = machine.Pin(19, machine.Pin.OUT)
display = spi_dotmatrix.Matrix8x8(hspi, ss, 2)
display.pixel(0,0,1)
display.show()
