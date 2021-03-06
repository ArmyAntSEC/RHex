from MotorController.MotorDriver import MotorDriver
from MotorController.PID import PID
from HomingEncoder.HomingEncoder import HomingEncoder
from TaskScheduler.IRecurringTask import IRecurringTask
from LogPrinter import LogPrinter
from NumericOutput import NumericOutput

class MotorController ( IRecurringTask ):
    def config(self, motorDriver: MotorDriver, homingEncoder: HomingEncoder, 
        Kp: float ):
        self.motorDriver = motorDriver
        self.homingEncoder = homingEncoder
        self.pid = PID(Kp=Kp)        
        self.enabled = False
        self.output = NumericOutput("controller")
        self.output.printHeaders( ("speed", "error", "Iterm", "motorPWM", "Position") )
        
    def setParams ( self, Kp, Ki ):
        self.pid.setParams( Kp, Ki )

    def setPoint( self, setPoint ):
        self.pid.setPoint = setPoint
    
    def enable(self):        
        self.enabled = True
    
    def disable(self):        
        self.enabled = False
    
    def run( self ):  
        if ( self.enabled ):      
            motorPWM = self.pid( self.homingEncoder.speed_cps )
            if ( motorPWM is None ):
                motorPWM = 0
            self.motorDriver.setMotorPWM( motorPWM )
            self.output( (self.homingEncoder.speed_cps, self.pid.error, 
                self.pid.ITerm, motorPWM, self.homingEncoder.position) )


