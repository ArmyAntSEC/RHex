from TaskScheduler.IRecurringTask import IRecurringTask

class TackScheduler:
    def __init__( self ):
        self.tasks = []

    def addTask( self, task: IRecurringTask ):
        self.tasks.append( task )
    
    def run(self):
        for task in self.tasks:
            if ( task.canRun() ):
                task.run()

    
