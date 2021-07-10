import utime
from TaskScheduler.IRecurringTask import IRecurringTask
from LogPrinter import LogPrinter

class IFutureTask(IRecurringTask):
    def __init__(self, waitTime_us: int, fun, taskScheduler ):
        IRecurringTask.__init__( self, waitTime_us)        
        self.fun = fun
        self.taskScheduler = taskScheduler        
        self.init()

    def run( self ):
        self.fun()    
        self.taskScheduler.deleteTask( self )                
            
