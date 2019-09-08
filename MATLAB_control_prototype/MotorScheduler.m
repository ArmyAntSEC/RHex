classdef MotorScheduler    
    properties
        wantedPositionLog;
    end
    
    methods
        function obj = MotorScheduler()
            obj.wantedPositionLog = TraceLogMat;
        end
    end
    
    methods
        function wantedPos = getWantedPos(obj,systemTime)
            loopTime = 1; %s
            locationInLoop = rem(systemTime,loopTime);
            
            % Should spend half of time between 0 and 0.3 rad
            if ( locationInLoop < 0.5 )
                wantedPos = (locationInLoop*2)*0.3;
            else
                wantedPos = 0.3 + ((locationInLoop - 0.5)*2)*(2*pi-0.3);
            end
            
            wantedPos = wantedPos + 2*pi*floor(systemTime/loopTime);
            
            obj.wantedPositionLog.append( wantedPos );
        end
    end
end

