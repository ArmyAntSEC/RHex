from machine import Pin
from machine import PWM
import utime

print ( "*************" )
print ( "Starting....." )
print ( "*************" )

encoder1 = Pin(6, Pin.IN )
encoder2 = Pin(7, Pin.IN )
breaker = Pin(28, Pin.IN )

position = 0
isHomed = False

def encoderHandler(pin):
    global position
    global isHomed
    position = position + 1
    #print ( "Position: ", position, " isHomed: ", isHomed )    

def breakerHandler(pin):
    global position
    global isHomed
    print ( "Homing: ", isHomed, " Postion: ", position  )
    position = 0
    if ( not isHomed ):        
        isHomed = True    

encoder1.irq ( trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=encoderHandler )
breaker.irq ( trigger=Pin.IRQ_RISING, handler=breakerHandler )

m1ena = Pin(3, Pin.OUT )
m1enb = Pin(4, Pin.OUT )
m1pwm = PWM(Pin(5))

m1ena.value(0)
m1enb.value(1)
m1pwm.freq(500)

m1pwm.duty_u16( 32000 )
utime.sleep(2)
m1pwm.duty_u16( 0 )