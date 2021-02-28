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

%% Move exactly one revolution
encoder.resetCount();
pcStored = [-0.0077 5.8579 -275.3214];
speed = 64;
drift = polyval( pcStored, speed );
board.writePWMDutyCycle( pins.MOTOR_PWM, speed/256 );
while ( encoder.readCount() < 48*74.83*0.92 - drift )
    pause(0.1);
    
end
disp ( encoder.readCount() );
board.writePWMDutyCycle( pins.MOTOR_PWM, 0 );

%%
encoder.resetCount();
pcStored = [-0.0077 5.8579 -275.3214];
speed = 64;
drift = polyval( pcStored, speed );
board.writePWMDutyCycle( pins.MOTOR_PWM, speed/256 );
while ( board.readDigitalPin( pins.OPTO ) == 1)
    pause(0.01);    
end
board.writePWMDutyCycle( pins.MOTOR_PWM, 0 );
disp ( encoder.readCount() );

    


