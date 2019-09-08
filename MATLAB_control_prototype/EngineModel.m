classdef EngineModel<handle
    
    properties(SetAccess=private)
        motorPositionRad;
        shaftPositionRad; 
        encoderOutputOne;
        encoderOutputTwo;
        inputPWM;
        
        motorPositionRadLog;
        shaftPositionRadLog; 
        encoderOutputOneLog;
        encoderOutputTwoLog;
        inputPWMLog;
    end
    
    methods
        function obj = EngineModel()
            obj.motorPositionRad = 0;
            obj.shaftPositionRad = 0;
            obj.encoderOutputOne = 0;
            obj.encoderOutputTwo = 0;
            obj.inputPWM = 0;      
            
            obj.motorPositionRadLog = TraceLogMat();
            obj.shaftPositionRadLog = TraceLogMat(); 
            obj.encoderOutputOneLog = TraceLogMat();
            obj.encoderOutputTwoLog = TraceLogMat();
            obj.inputPWMLog = TraceLogMat();
        end
        
        function step(obj)
            motorSpeedRadPerSecond = GlobalParams.noLoadMotorMaxSpeedRadPerSecond * obj.inputPWM/256;
            obj.motorPositionRad = obj.motorPositionRad + GlobalParams.physicsTimeDelta*motorSpeedRadPerSecond;
            obj.shaftPositionRad = obj.motorPositionRad / GlobalParams.shaftToMotorRatio;
            obj.encoderOutputOne = sin(obj.motorPositionRad*GlobalParams.encoderToMotorRatio)>0;
            obj.encoderOutputTwo = cos(obj.motorPositionRad*GlobalParams.encoderToMotorRatio)>0;            

            obj.motorPositionRadLog.append( obj.motorPositionRad );
            obj.shaftPositionRadLog.append( obj.shaftPositionRad );
            obj.encoderOutputOneLog.append( obj.encoderOutputOne );
            obj.encoderOutputTwoLog.append( obj.encoderOutputTwo );
            obj.inputPWMLog.append( obj.inputPWM );
        end
        
        function setInputPWM( obj, pwm )
            assert ( pwm >-256 && pwm < 256 );
            obj.inputPWM = pwm;
        end
    end
end

