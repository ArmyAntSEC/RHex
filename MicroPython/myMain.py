from MotorController.MotorDriver import MotorDriver
from machine import Pin
from machine import PWM
from sys import exit
import utime
from TaskScheduler.TaskScheduler import TackScheduler
from TaskScheduler.IRecurringTask import IRecurringTask
from TaskScheduler.IFutureTask import IFutureTask
from NonBlockingRead import NonBlockingRead

class Beacon(IRecurringTask):
    def run( self ):
        print ( "Time: " , utime.ticks_us() )

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
        self.taskScheduler.addTask( Beacon(1000000) )
        
        self.commands = {
            "info": self.cmdInfo,
            "simpleMove": self.cmdSimpleMove,
            "stats": self.cmdStats,
            "exit": self.cmdExit            
        }

        # Start the infitine loop
        self.run()


    def commandParser( self, command: str ):
        """Parses a single input command. Should return immediately"""
        if  ( command in self.commands ):
            self.commands[command]()
        else:
            print ( "Unknown command: ", command )
            print ( "Supported commands:" )
            for key in self.commands.keys(): 
                print ( "- ", key )
                
            

    def run(self): 
        print ( "Running loop" )
        reader = NonBlockingRead( self.commandParser )

        while True:        
            reader()
            self.taskScheduler.run()            

    def cmdInfo(self):
        print ( "This is the info" )
    
    def cmdSimpleMove(self):
        print ( "Doing a simple move" ); 
        self.driver1.setMotorPWM(0.5)                
        
        def stopFun():
            self.driver1.setMotorPWM(0)            
            print ( "Done with simple move" );         
        self.taskScheduler.addTask( IFutureTask(1000,stopFun,self.taskScheduler) )

    def cmdStats(self):
        self.taskScheduler.printStats()

    def cmdExit(self):
        exit()

mainFunc()
