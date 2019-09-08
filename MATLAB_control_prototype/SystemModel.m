classdef SystemModel<handle
    %SYSTEMMODEL Summary of this class goes here
    %   Detailed explanation goes here
    
    properties                
        stepCount;                
        encoderReaderOne;
        motorRegulator;
        motorScheduler;
    end
    
    methods
        function obj = SystemModel()                          
            obj.stepCount = 0;            
            obj.encoderReaderOne = EncoderReader();
            obj.motorRegulator = MotorRegulator();
            obj.motorScheduler = MotorScheduler();
        end
        
        function step(obj, physicsModel)           
            obj.stepCount = obj.stepCount + 1;
            
            %Read the encoder
            encoderValueOne = physicsModel.engineOne.encoderOutputOne;
            encoderValueTwo = physicsModel.engineOne.encoderOutputTwo;
            obj.encoderReaderOne.step( encoderValueOne, encoderValueTwo );
            
            % Read the wanted position
            systemClock = physicsModel.systemClock;
            wantedPosition = obj.motorScheduler.getWantedPos( systemClock );
            
            %Regulate the motor power
            motorPosition = obj.encoderReaderOne.getPosition();
            pwm = obj.motorRegulator.step(motorPosition, wantedPosition);
            physicsModel.engineOne.setInputPWM( pwm );
            
            
        end
    end
end

