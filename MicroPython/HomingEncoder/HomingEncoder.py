from machine import Pin

class HomingEncoder:
    def __init__(self):
        self.position = int(0)
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
        print ( "Homing: ", self.isHomed, " Postion: ", self.position  )        
        if ( not self.isHomed ):        
            self.isHomed = True    
            self.position = 0
    
    def unHome(self):
        self.isHomed = False
    