%% Lock and load
clear;
clc;

%% Init the interface
clear ( 'board' );
board = arduino();
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

encoder = board.rotaryEncoder( pins.ENCODER_1, pins.ENCODER_2 );

%% Do the thing
speeds = repmat(64:32:256,1,50);
data = nan(20,2,numel(speeds));

for ii = 1:numel(speeds)
    board.writePWMDutyCycle( pins.MOTOR_PWM, speeds(ii)/256 );
    pause ( 2 );
    board.writePWMDutyCycle( pins.MOTOR_PWM, 0 );
    tic;
    for jj = 1:20
        data(jj,1,ii) = encoder.readCount();
        data(jj,2,ii) = toc;        
    end    
end
%%
drift = nan(numel(speeds),1);
subplot ( 2, 1, 1 );
for ii = 1:size(data,3)
    plot ( data(:,2,ii), data(:,1,ii)-max(data(:,1,ii)) );
    drift(ii) = max(data(:,1,ii)) - min(data(:,1,ii)); 
    hold on;
end
%%
pc = polyfit( speeds, drift, 2 );
subplot ( 2, 1, 2 );
plot ( speeds, drift, '.', [0 speeds(1:7)], polyval(pc, [0 speeds(1:7)]), '-' )
ax = axis;
axis( [0 ax(2) 0 ax(4)] );





