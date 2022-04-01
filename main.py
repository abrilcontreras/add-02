from machine import Pin, ADC
import time
adc = ADC (Pin(26))
vol1=0
temp1=0
while 1:
    adc1 = adc.read_u16()
    vol1 = adc1 * 3.3
    vol1 = vol1/65535
    temp1 = vol1/0.01
    print("El valor de la Temperatura es: {:.2f}°C" .format(temp1))
    time.sleep(1)
