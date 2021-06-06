from machine import ADC
from machine import PWM
import utime

breaker = ADC(28 )

while True:
    value = breaker.read_u16()
    print ( "Breaker: ", value )
    utime.sleep(0.5)