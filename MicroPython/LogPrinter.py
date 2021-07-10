from utime import ticks_ms
from utime import ticks_diff

class LogPrinterClass:
    def __init__(self):
        self.startTime_ms = ticks_ms()

    def __call__( self, *arg ):
        print ( "[" + str(ticks_diff(ticks_ms(), self.startTime_ms)) + "] ", *arg )

logPrinter = LogPrinterClass()

def LogPrinter( *arg ):
    logPrinter( *arg )