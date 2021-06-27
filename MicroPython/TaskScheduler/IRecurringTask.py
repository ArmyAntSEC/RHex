import utime

class IRecurringTask:
    def __init__(self, period: int):
        self.period = period
        self.init()

    def init(self ):
        self.next_time = utime.ticks_add( utime.ticks_us(), self.period )

    def canRun( self ):
        return utime.ticks_diff( utime.ticks_us(), self.next_time ) < 0

    def run( self ):
        print ( "IRecurringTask needs to be inherited and the run() shall be overridden." )
            
