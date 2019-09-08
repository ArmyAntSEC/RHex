classdef GlobalParams
    %GLOBALPARAMS Summary of this class goes here
    %   Detailed explanation goes here
    
    properties(Constant)
        physicsTimeDelta = 1e-5;
        totalLoops = 2e5;
        systemTimeDelta = 1e-5;
    end
    
    properties(Constant)
        shaftToMotorRatio = 74.83;
        encoderToMotorRatio = 48/4;
        noLoadMotorMaxSpeedRadPerSecond = 9727.9*pi/30;
    end
    
    methods
        function obj = GlobalParams()
        end
    end
end

