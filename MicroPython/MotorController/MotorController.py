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
        
    def setPoint( self, setPoint ):
        self.pid.setpoint = setPoint
    
    def run( self ):        
        motorPWM = self.pid( self.homingEncoder.position )
        self.motorDriver.setMotorPWM( motorPWM )


