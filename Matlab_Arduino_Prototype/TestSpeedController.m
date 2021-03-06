%% Lock and load
% http://brettbeauregard.com/blog/2011/04/improving-the-beginner%e2%80%99s-pid-derivative-kick/
clear;
clc;

%% Init the interface
clear ( 'board' );
board = arduino('COM4','Uno','Libraries','rotaryEncoder');
disp ( board );

%% Pin mapping
pins.MOTOR_EN1 = 'D4';
pins.MOTOR_EN2 = 'D5';
pins.MOTOR_CS = 'A0';
pins.ENCODER_1 = 'D2';
pins.ENCODER_2 = 'D3';
pins.OPTO = 'D7';
pins.MOTOR_PWM = 'D6';

%% Setup
board.configurePin( pins.MOTOR_EN1, 'DigitalOutput' );
board.configurePin( pins.MOTOR_EN2, 'DigitalOutput' );
board.configurePin( pins.MOTOR_PWM, 'PWM' );

board.writeDigitalPin( pins.MOTOR_EN1, 1 );
board.writeDigitalPin( pins.MOTOR_EN2, 0 );

encoder = board.rotaryEncoder( pins.ENCODER_1, pins.ENCODER_2,  3592/4 );

%% Move a bit 
len = 50;
powerLog = nan(len,1);
speedLog = powerLog;
timeLog = powerLog;

P = 6;
D = 2;
Input = 0;
Output = 0;
Setpoint = 20;
lastInput = 0;

tic;
for ii = 1:len
    time = toc;
    Input = encoder.readSpeed();
    Error = Setpoint - Input;
    dInput = Input - lastInput;
    lastInput = dInput;
    
    Output = P*Error + D*dInput;
    
    Output = min(max(0,Output),255);
    board.writePWMDutyCycle( pins.MOTOR_PWM, Output/256 );
    speedLog(ii) = Input;
    powerLog(ii) = Output;
    timeLog(ii) = time;    
    fprintf ( '.' );
end
fprintf ( '\n' );

board.writePWMDutyCycle( pins.MOTOR_PWM, 0 );
%%
subplot ( 2, 1, 1 );
plot ( timeLog, speedLog, timeLog, Setpoint*ones(size(timeLog)) );
title ( 'Speed' );
subplot ( 2, 1, 2 );
plot ( timeLog, powerLog );
title ( 'Power' );