%% Lock and Load
clear;
clc;

%% Open the device
dev = serialport ( 'COM4', 115200 ); 
dev.configureTerminator( 'CR' );
pause(2);
targetSpeed = 5000;
dev.write ( [0.5 0 2 targetSpeed], 'single' );

%% Load the data
pause(3);
chars = dev.NumBytesAvailable;
raw = dev.read( chars, 'char' );

%% Parse the data
[C,P] = textscan( raw, '%s', 2, 'Delimiter', ',' );
D = textscan( raw((P+1):end), '%s %s', 'Delimiter', ',' );
data = table ( str2double(D{1,1}), str2double(D{1,2}), 'VariableNames', C{1} );
data.Time = (1:height(data))'*0.01;

%% Now look at the data
subplot ( 3, 1, 1 );
plot ( data.Time, data.Speed, [0 max(data.Time)], targetSpeed*[1 1] );
title ( 'Speed' );
subplot ( 3, 1, 2 );
plot ( data.Time, data.Power, data.Time(1:end-1), diff(data.Speed)/5 );
title ( 'Power' );
subplot ( 3, 1, 3 );
plot ( data.Time(1:end-2), diff(diff(data.Speed)) );
title ( 'Jerk' );

clear('dev');
disp ( 'Done' );