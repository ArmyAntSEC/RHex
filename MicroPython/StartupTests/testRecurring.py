import utime

lastTime_ms = utime.ticks_ms()
nextTime_ms = utime.ticks_add( lastTime_ms, 100 )

lastTime_us = utime.ticks_us()
intervalMean = 0
intervalMeanSq = 0
callCount = 0

while ( True ):
    # This block of code is the problem. It sometimes takes more than 1ms, up to 5ms
    thisTime_us = utime.ticks_us()
    delta_us = utime.ticks_diff( thisTime_us, lastTime_us )
    intervalMean = (callCount*intervalMean + delta_us)/(callCount+1)
    intervalMeanSq = (callCount*intervalMeanSq + delta_us*delta_us)/(callCount+1)
    lastTime_us = thisTime_us
    callCount = callCount + 1
    # End of problem block

    thisTime_ms = utime.ticks_ms()

    if ( utime.ticks_diff( nextTime_ms, thisTime_ms ) < 0 ):
        timeDiff_ms = utime.ticks_diff( thisTime_ms, lastTime_ms)
        print ( "Time: ", thisTime_ms , " Time diff: ", timeDiff_ms, end='' )
        if ( timeDiff_ms != 100 ):
            print ( " Warning!" )
        else:
            print ()
        lastTime_ms = thisTime_ms
        nextTime_ms = utime.ticks_add( nextTime_ms, 100 )