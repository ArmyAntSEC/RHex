from machine import Pin
import utime
from TaskScheduler.IRecurringTask import IRecurringTask

class HomingEncoder(IRecurringTask):
    def __init__(self, period_us: int):
        IRecurringTask.__init__(self, period_us)
        self.position = int(0)
        self.lastPosition = int(0)
        self.lastTime_us = utime.ticks_us()
        self.speed_cps = 0
        self.isHomed = False

    def config( self, encoder1: int, encoder2: int, homing: int ):
        self.encoder1 = Pin(encoder1, Pin.IN )
        self.encoder2 = Pin(encoder2, Pin.IN )
        self.homing = Pin(homing, Pin.IN )
        
        self.encoder1.irq ( trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=self.encoderHandler )
        self.homing.irq ( trigger=Pin.IRQ_RISING, handler=self.homingHandler )

    def encoderHandler(self, pin: Pin):
        self.position = self.position + 1        

    def homingHandler(self, pin: Pin):
        print ( "Homing: ", self.isHomed, " Postion: ", self.position, " Speed: ", self.speed_cps  )        
        if ( not self.isHomed ):        
            self.isHomed = True    
            self.position = 0        
    
    def unHome(self):
        self.isHomed = False
    
    def forceHomed(self):
        self.isHomed = True
    
    def run(self):
        # Get the current position and time
        thisPos = self.position
        thisTime_us = utime.ticks_us()
        
        # Compute the deltas
        posDelta = thisPos - self.lastPosition
        timeDelta_us = utime.ticks_diff( thisTime_us, self.lastTime_us)
        timeDelta_s = timeDelta_us / 1e6

        # Compute the speed
        self.speed_cps = posDelta / timeDelta_s

        #Store the time and pos when the last measurement was made
        self.lastPosition = thisPos
        self.lastTime_us = thisTime_us
        
