import utime
#from TaskScheduler.TaskScheduler import TaskScheduler

class IFutureTask:
    def __init__(self, waitTime_us: int, fun, taskScheduler ):
        self.waitTime_us = waitTime_us
        self.fun = fun
        self.taskScheduler = taskScheduler        
        self.init()

    def init(self ):
        timeNow_us = utime.ticks_us()
        self.nextTime_us = utime.ticks_add( timeNow_us, self.waitTime_us )
        print ( "Init time: ", timeNow_us )
        print ( "Next time: ", timeNow_us )

    def canRun( self ):
        return utime.ticks_diff( utime.ticks_us(), self.nextTime_us ) < 0

    def run( self ):
        self.fun()    
        self.taskScheduler.deleteTask( self )
        timeNow_us = utime.ticks_us()
        print ( "Run time: ", timeNow_us )
            
