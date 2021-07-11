
class PID(object):
    """A simple PID controller."""

    def __init__( self, Kp=1.0, Ki=0.0, setPoint=0.0, dT=0.01 ):
        self.dT = dT

        self.Kp = Kp
        self.Ki = Ki*self.dT
        
        self.setPoint = setPoint        
        self.error = 0        
        self.ITerm = 0        

    def __call__(self, input):        
        # Compute error terms
        self.error = self.setPoint - input        

        # Compute the integral
        self.ITerm = self.ITerm + ( self.Ki * self.error )
        self.ITerm = self.clamp( self.ITerm )
        
        # Compute final output
        output = self.Kp * self.error + self.ITerm
        output = self.clamp(output)        

        return output

    def clamp( self, value ):
        minOutput = GetPowerForFreeSpeed( self.setPoint ) * 0.6
        if ( value < minOutput ):
            return minOutput
        elif ( value > 1 ):
            return 1
        else:
            return value

    def setParams ( self, Kp, Ki ):
        self.Kp = Kp
        self.Ki = Ki*self.dT

def GetPowerForFreeSpeed( wantedSpeed: float ) -> float:
    power = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    speed = [1200, 2000, 2500, 2950, 3300, 3500, 3650, 3800, 4100]

    if ( wantedSpeed < speed[0] ):
        return 0

    for i in range(1,len(speed)-1):
        if speed[i] > wantedSpeed:
            x1 = speed[i-1]
            x2 = speed[i]
            y1 = power[i-1]
            y2 = power[i]
            xRem = (wantedSpeed - x1)/(x2-x1)
            y = y1 + (y2-y1)*xRem
            return y

    return power[-1]

    
