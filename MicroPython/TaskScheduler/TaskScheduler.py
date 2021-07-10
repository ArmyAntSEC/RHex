from TaskScheduler.IRecurringTask import IRecurringTask
import utime
from math import sqrt
from LogPrinter import LogPrinter

class TackScheduler:
    def __init__( self ):
        self.tasks = []
        self.lastTime_us = utime.ticks_us()
        self.intervalMean = 0
        self.intervalMeanSq = 0
        self.callCount = 0

    def addTask( self, task: IRecurringTask ):
        self.tasks.append( task )
    
    def deleteTask( self, task: IRecurringTask ):
        self.tasks.remove( task )

    def run(self):
        # Compute the call frequency statistics
        thisTime_us = utime.ticks_us()
        delta_us = utime.ticks_diff( thisTime_us, self.lastTime_us )
        self.intervalMean = (self.callCount*self.intervalMean + delta_us)/(self.callCount+1)
        self.intervalMeanSq = (self.callCount*self.intervalMeanSq + delta_us*delta_us)/(self.callCount+1)
        self.lastTime_us = thisTime_us
        self.callCount = self.callCount + 1

        for task in self.tasks:
            if ( task.canRun() ):                
                task.run()
        

    def printStats(self):    
        LogPrinter ( "Mean time between calls: ", "{:.2f}".format( self.intervalMean/1000 ), 
            " ms. (Should be ~0.2 ms)" )
        LogPrinter ( "Standard deviation of time between calls in percent: ", 
            "{:.2f}".format( 100* sqrt( (self.intervalMeanSq/self.callCount - 
            self.intervalMean*self.intervalMean / (self.callCount * self.callCount ) ) ) / self.intervalMean ),
            " %. (Should be ~1%)" )
