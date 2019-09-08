classdef EncoderReader<handle
    properties ( Constant )
        filterConstant = 100;
    end
    
    properties(Access=private)
        lastValueOne;
        lastValueTwo;
        lastPosition;         
        
        lastPositionFiltered;
        
        transitionsMatrix                
    end
    
    properties
        lastPositionLog; 
        lastPositionFilteredLog;
    end
    
    methods
        function obj = EncoderReader()
            obj.lastValueOne = 0;
            obj.lastValueTwo = 1;
            obj.lastPosition = 0;
            obj.lastPositionFiltered = 0;
            
            obj.transitionsMatrix = zeros(2,2,2,2);
            obj.transitionsMatrix(2,2,1,2) = 1;
            obj.transitionsMatrix(1,2,1,1) = 1;
            obj.transitionsMatrix(1,1,2,1) = 1;
            obj.transitionsMatrix(2,1,2,2) = 1;
            obj.transitionsMatrix(2,2,2,1) = -1;
            obj.transitionsMatrix(2,1,1,1) = -1;
            obj.transitionsMatrix(1,1,1,2) = -1;
            obj.transitionsMatrix(1,2,2,2) = -1;
            
            obj.lastPositionLog = TraceLogMat;
            obj.lastPositionFilteredLog = TraceLogMat;
        end
        
        function step(obj,valueOne,valueTwo)
            stepDir = -obj.transitionsMatrix( ...
                obj.lastValueOne+1, obj.lastValueTwo+1, ...
                valueOne+1, valueTwo+1 );
            stepAngleRad = stepDir / GlobalParams.encoderToMotorRatio/(2*pi);           
            
            obj.lastValueOne = valueOne;
            obj.lastValueTwo = valueTwo;
            
            obj.lastPosition = obj.lastPosition + stepAngleRad;
            obj.lastPositionFiltered = ...
                (obj.lastPositionFiltered*(EncoderReader.filterConstant-1) + ...
                obj.lastPosition) / EncoderReader.filterConstant;
          
            
            obj.lastPositionLog.append( obj.lastPosition );
            obj.lastPositionFilteredLog.append( obj.lastPositionFiltered );
        end
        
        function pos = getPosition(obj)
            pos = obj.lastPositionFiltered;
        end
    end
end

