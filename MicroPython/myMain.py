from MotorController.MotorDriver import MotorDriver
from MotorController.MotorController import MotorController
from HomingEncoder.HomingEncoder import HomingEncoder
from machine import Pin
from machine import PWM
from sys import exit
from TaskScheduler.TaskScheduler import TackScheduler
from TaskScheduler.IRecurringTask import IRecurringTask
from TaskScheduler.IFutureTask import IFutureTask
from NonBlockingRead import NonBlockingRead
from LogPrinter import LogPrinter
from NumericOutput import NumericOutput

class Beacon(IRecurringTask):
    def __init__(self):
        IRecurringTask.__init__(self, 10000000)

    def run( self ):
        LogPrinter ( "Beacon!" )

class mainFunc:
    def __init__( self ):                    
        num = NumericOutput( "hello" )
        num( (1, 2) )

        m1ena = Pin(3, Pin.OUT )
        m1enb = Pin(4, Pin.OUT )
        m1pwm = PWM(Pin(5))
        m1pwm.freq(1000)    

        self.driver1 = MotorDriver()
        self.driver1.config( m1ena, m1enb, m1pwm )        

        self.homingEncoder1 = HomingEncoder(10000)
        self.homingEncoder1.config(6,7,28)

        self.controller1 = MotorController(10000)
        self.controller1.config( self.driver1, self.homingEncoder1, 0.0003 )
        
        self.taskScheduler = TackScheduler()   
        self.taskScheduler.addTask( Beacon() )
        self.taskScheduler.addTask( self.controller1 )
        self.taskScheduler.addTask( self.homingEncoder1 )
        
        self.commands = {
            "info": self.cmdInfo,
            "simpleMove": self.cmdSimpleMove,
            "const": self.cmdMoveAtConstantSpeed,
            "stats": self.cmdStats,
            "exit": self.cmdExit            
        }

        # Start the infitine loop
        self.run()


    def commandParser( self, command: str ):
        """Parses a single input command. Should return immediately"""
        commandTokens = str.split( command )
        #LogPrinter ( commandTokens )

        if  ( commandTokens[0] in self.commands ):
            arguments = [float(i) for i in commandTokens[1:]]
            #LogPrinter( arguments )
            self.commands[commandTokens[0]](arguments)
        else:
            LogPrinter ( "Unknown command: ", command )
            LogPrinter ( "Supported commands:" )
            for key in self.commands.keys(): 
                LogPrinter ( "- ", key )                            

    def run(self): 
        LogPrinter ( "Running loop" )
        reader = NonBlockingRead( self.commandParser )

        while True:        
            reader()
            self.taskScheduler.run()            

    def cmdInfo(self, args):
        LogPrinter ( "This is the info" )
    
    def cmdSimpleMove(self, args ):
        LogPrinter ( "Doing a simple move" ); 
        power = 0.25
        if ( len(args) > 0 ):
            power = args[0]
        self.driver1.setMotorPWM(power)                
        
        def stopFun():
            self.driver1.setMotorPWM(0)            
            LogPrinter ( "Done with simple move" );         
        self.taskScheduler.addTask( IFutureTask(int(4e6),stopFun,self.taskScheduler) )

    def cmdMoveAtConstantSpeed(self, args):
        LogPrinter ( "Moving at constant speed" );                         
        speed = 2000
        if ( len(args) > 0 ):
            speed = args[0]

        self.controller1.setPoint(speed)
        self.controller1.enable()
        # Force homing.
        self.homingEncoder1.forceHomed()

        LogPrinter( "Speed setpoint: ", speed )

        def stopFun():
            self.controller1.disable()
            self.driver1.setMotorPWM(0)            
            LogPrinter ( "Done miving at constant speed" );         
        self.taskScheduler.addTask( IFutureTask(int(1e6),stopFun,self.taskScheduler) )

    def cmdStats(self, args):
        self.taskScheduler.printStats()

    def cmdExit(self, args):
        self.driver1.setMotorPWM(0)
        exit()

mainFunc()
