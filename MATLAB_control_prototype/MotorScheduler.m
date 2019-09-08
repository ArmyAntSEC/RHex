classdef MotorScheduler    
    properties
        wantedShaftPositionRevLog;
    end
    
    methods
        function obj = MotorScheduler()
            obj.wantedShaftPositionRevLog = TraceLogMat;
        end
    end
    
    methods
        function wantedShaftPosRev = getWantedShaftPosRev(obj,systemTime)
            loopTime = 1; %s
            locationInLoop = rem(systemTime,loopTime);
            
            % Should spend half of time between 0 and 0.1 rev
            if ( locationInLoop < 0.5 )
                wantedShaftPosRev = (locationInLoop*2)*0.1;
            else
                wantedShaftPosRev = 0.1 + ((locationInLoop - 0.5)*2)*(1-0.1);
            end
            
            wantedShaftPosRev = wantedShaftPosRev + floor(systemTime/loopTime);
            
            obj.wantedShaftPositionRevLog.append( wantedShaftPosRev );
        end
    end
end

