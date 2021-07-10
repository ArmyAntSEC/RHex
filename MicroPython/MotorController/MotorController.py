from MotorController.MotorDriver import MotorDriver
from MotorController.PID import PID
from HomingEncoder.HomingEncoder import HomingEncoder
from TaskScheduler.IRecurringTask import IRecurringTask
from LogPrinter import LogPrinter

class MotorController ( IRecurringTask ):
    def config(self, motorDriver: MotorDriver, homingEncoder: HomingEncoder, 
        P: float ):
        self.motorDriver = motorDriver
        self.homingEncoder = homingEncoder
        self.pid = PID(Kp=P)        
        self.enabled = False
        
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
            LogPrinter ( "Speed: ", self.homingEncoder.speed_cps , " Power: ", motorPWM )


