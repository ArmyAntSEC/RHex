from MotorController.MotorDriver import MotorDriver
from machine import Pin
from machine import PWM
from sys import exit
import utime
from TaskScheduler.TaskScheduler import TackScheduler
from NonBlockingRead import NonBlockingRead

class mainFunc:
    def __init__( self ):
        print ( "Hello Again World!" )    
            
        m1ena = Pin(3, Pin.OUT )
        m1enb = Pin(4, Pin.OUT )
        m1pwm = PWM(Pin(5))
        m1pwm.freq(1000)    

        self.driver1 = MotorDriver()
        self.driver1.config ( m1ena, m1enb, m1pwm )

        self.taskScheduler = TackScheduler()   
        
        # Start the infitine loop
        self.run()


    def commandParser( self, command: str ):
        """Parses a single input command. Should return immediately"""

        if ( command == "info" ):        
            print ( "This is the info" )

        elif ( command == "simpleMove" ):
            print ( "Doing a simple move" ); 
            self.driver1.setMotorPWM(0.5)
            #sleep(1)
            self.driver1.setMotorPWM(0)            
            print ( "Done with simple move" ); 
        
        elif ( command == "stats" ):
            self.taskScheduler.printStats()

        elif ( command == "exit" ):
            # Exit the program
            exit()
        else:
            print ( "Unknown command: ", command )


    def run(self): 
        print ( "Running loop" )
        reader = NonBlockingRead( self.commandParser )

        while True:        
            reader()
            self.taskScheduler.run()            


mainFunc()
