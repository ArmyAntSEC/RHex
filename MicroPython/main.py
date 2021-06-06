from motorController.motorDriver import MotorDriver
from machine import Pin
from machine import PWM
from utime import sleep

def mainFunc(): 
    print ( "Hello World!" )    

    m1ena = Pin(3, Pin.OUT )
    m1enb = Pin(4, Pin.OUT )
    m1pwm = PWM(Pin(5))
    m1pwm.freq(1000)    

    driver1 = MotorDriver()
    driver1.config ( m1ena, m1enb, m1pwm )

    while True:
        command = input ( "$ " )    
        
        if ( command == "info" ):        
            print ( "This is the info" )
        elif ( command == "simpleMove" ):
            print ( "Doing a simple move" ); 
            driver1.setMotorPWM(0.5)
            sleep(1)
            driver1.setMotorPWM(0)
            print ( "Done with simple move" ); 
        else:
            print ( "Unknown command: ", command )

mainFunc()
