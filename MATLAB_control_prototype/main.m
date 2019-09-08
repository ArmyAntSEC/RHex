%% Lock and load
clc;
clear;

%% Do the setup
physicsModel = PhysicsModel();
systemModel = SystemModel();

%% Start the loop
t = tic;

for ii = 1:GlobalParams.totalLoops                                   
    physicsModel.step();   
    
    if ( rem(ii, 10) == 0 )
        systemModel.step(physicsModel);
    end
end

endTime = toc(t);
fprintf ( "Time to run: %0.2fs. Loops/s: %0.2f.\n", endTime, GlobalParams.totalLoops/endTime );

%% Plot data of interest
physicsTimeScale = (1:GlobalParams.totalLoops)*GlobalParams.physicsTimeDelta;
systemTimeScale = (1:(GlobalParams.totalLoops/10))*GlobalParams.systemTimeDelta;

subplot ( 2,2,1)
title ( 'Motor actual position [rad]' )
plot ( physicsTimeScale, physicsModel.engineOne.motorPositionRadLog.data/(2*pi) );

subplot ( 2,2,2)
title ( 'Driver input PWM value' );
plot ( physicsTimeScale, physicsModel.engineOne.inputPWMLog.data );

subplot ( 2,2,3)
title ( 'Encoder output' );
plot ( physicsTimeScale, physicsModel.engineOne.encoderOutputOneLog.data, ...
    physicsTimeScale, physicsModel.engineOne.encoderOutputTwoLog.data );

subplot ( 2,2,4)
title ( 'Encoder measured position' );
plot ( systemTimeScale, systemModel.encoderReaderOne.lastPositionLog.data, '.-', ...
    systemTimeScale, systemModel.encoderReaderOne.lastPositionFilteredLog.data, '.-', ...
    systemTimeScale, systemModel.motorScheduler.wantedPositionLog.data, '--' )