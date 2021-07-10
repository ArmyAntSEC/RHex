from LogPrinter import LogPrinter

class MotorDriver:
    def config(self, pinEnable1, pinEnable2, pinPwm ):
        self.pinEnable1 = pinEnable1
        self.pinEnable2 = pinEnable2
        self.pinPwm = pinPwm
        self.lastPwmValue = 0

        self.setMotorPWM(0)
    
    def setMotorPWM( self, pwmValue ):
        #LogPrinter ( "pwmValue: ", pwmValue )
        #LogPrinter ( "lastPWM: ", self.lastPwmValue)  

        if ( pwmValue < 0 or ( pwmValue == 0 and self.lastPwmValue > 0 ) ):
            self.pinEnable1.value(0)
            self.pinEnable2.value(1)
        elif ( pwmValue > 0 or ( pwmValue == 0 and self.lastPwmValue < 0 ) ):
            self.pinEnable1.value(1)
            self.pinEnable2.value(0)
        else:
            self.pinEnable1.value(0)
            self.pinEnable2.value(0)
        
        self.pinPwm.duty_u16( int(pwmValue*(2**16)) )




        
    
