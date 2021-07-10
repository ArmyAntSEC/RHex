import utime

class IRecurringTask:
    def __init__(self, period_us: int ):        
        self.period_us = period_us        
        self.init()

    def init(self ):
        self.nextTime_us = utime.ticks_add( utime.ticks_us(), self.period_us )

    def canRun( self ):
        return utime.ticks_diff( utime.ticks_us(), self.nextTime_us ) < 0

    def run( self ):
        print ( "IRecurringTask needs to be inherited and the run() shall be overridden." )
            
