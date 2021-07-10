
class PID(object):
    """A simple PID controller."""

    def __init__( self, Kp=1.0, setPoint=0, dT = 0.01, outputLimits=(0,1) ):
        self.Kp = Kp
        self.setPoint = setPoint
        self.outputLimits = outputLimits
        self.dT = dT

    def __call__(self, input):
        
        # Compute error terms
        error = self.setPoint - input        

        # Regular proportional-on-error, simply set the proportional term
        self.proportional = self.Kp * error

        # Compute final output
        output = self.proportional
        output = self.clamp(output)        

        return output

    def clamp( self, value ):
        if ( value < self.outputLimits[0] ):
            return self.outputLimits[0]
        elif ( value > self.outputLimits[1] ):
            return self.outputLimits[1]
        else:
            return value
