from MotorController.MotorDriver import MotorDriver
from MotorController.PID import PID
from HomingEncoder.HomingEncoder import HomingEncoder
from TaskScheduler.IRecurringTask import IRecurringTask

class MotorController ( IRecurringTask ):
    def config(self, motorDriver: MotorDriver, homingEncoder: HomingEncoder, 
        P: float, D: float, I: float ):
        self.motorDriver = motorDriver
        self.homingEncoder = homingEncoder
        self.pid = PID()
        self.pid.auto_mode = False
        self.enabled = False
        
    def setPoint( self, setPoint ):
        self.pid.setpoint = setPoint
    
    def enable(self):
        self.pid.auto_mode = True
        self.enabled = True
    
    def disable(self):
        self.pid.auto_mode = True
        self.enabled = False
    
    def run( self ):  
        if ( self.enabled ):      
            motorPWM = self.pid( self.homingEncoder.position )
            if ( motorPWM is None ):
                motorPWM = 0
            self.motorDriver.setMotorPWM( motorPWM )


