from machine import Pin
from machine import PWM
import utime

m1ena = Pin(3, Pin.OUT )
m1enb = Pin(4, Pin.OUT )
m1pwm = PWM(Pin(5))

m1ena.value(0)
m1enb.value(1)
m1pwm.freq(500)

for i in range(4):    
    power = i*4096*4
    m1pwm.duty_u16( power )
    print ( "Step: ", i, " Power: ", power )
    utime.sleep(1)

m1pwm.duty_u16(0)
