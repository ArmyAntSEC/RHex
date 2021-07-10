from utime import ticks_ms
from utime import ticks_diff

class NumericOutput:
    def __init__(self, id):
        self.startTime_ms = ticks_ms()
        self.id = id

    def __call__( self, *arg ):        
        print ( "#" + self.id, (ticks_diff(ticks_ms(), self.startTime_ms),) + arg[0]  )        

    def printHeaders( self, headers ):
        print ( "#" + self.id, ("time_ms",) + headers )        
