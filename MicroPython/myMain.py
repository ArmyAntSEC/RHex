from MotorController.MotorDriver import MotorDriver
from machine import Pin
from machine import PWM
import utime
from TaskScheduler.TaskScheduler import TackScheduler
from NonBlockingRead import NonBlockingRead

#import sys,uselect
#poll=uselect.poll()
#spoll.register(sys.stdin,uselect.POLLIN)
#def read1():
#    #return(sys.stdin.read(1) if spoll.poll(0) else None)
#    print ( "Anyting?" )
#    if ( spoll.poll(0) ):
#        print ( "Got one: ", sys.stdin.read(1) )

    
def mainFunc(): 
    print ( "Hello Again World!" )    

    reader = NonBlockingRead()

    while True:        
        reader()
        
    m1ena = Pin(3, Pin.OUT )
    m1enb = Pin(4, Pin.OUT )
    m1pwm = PWM(Pin(5))
    m1pwm.freq(1000)    

    driver1 = MotorDriver()
    driver1.config ( m1ena, m1enb, m1pwm )

    taskScheduler = TackScheduler()        

    while True:
        taskScheduler.run()

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
