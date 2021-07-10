import utime
from LogPrinter import LogPrinter

class IRecurringTask:
    def __init__(self, period_us: int ):
        self.period_us = period_us
        self.init()

    def init(self):        
        thisTime_us = utime.ticks_us()
        self.nextTime_us = utime.ticks_add( thisTime_us, self.period_us )

    def canRun( self ):
        thisTime_us = utime.ticks_us()
        timeDiff_us = utime.ticks_diff( self.nextTime_us, thisTime_us )                
        if ( timeDiff_us < 0 ):
            self.nextTime_us = utime.ticks_add( self.nextTime_us, self.period_us )
            return True    
        else:
            return False

    def run( self ):
        LogPrinter ( "IRecurringTask needs to be inherited and the run() shall be overridden." )
            
