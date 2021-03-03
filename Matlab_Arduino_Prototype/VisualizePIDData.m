%% Lock and Load
clear;
clc;

%% Open the device
dev = serialport ( 'COM4', 115200 ); 
dev.configureTerminator( 'CR' );
pause(2);
dev.write ( 0, 'uint8' );

%% Load the data
pause(2);
chars = dev.NumBytesAvailable;
raw = dev.read( chars, 'char' );

%% Parse the data
[C,P] = textscan( raw, '%s', 2, 'Delimiter', ',' );
D = textscan( raw((P+1):end), '%s %s', 'Delimiter', ',' );
data = table ( str2double(D{1,1}), str2double(D{1,2}), 'VariableNames', C{1} );
data.Time = (1:height(data))'*0.01;

%% Now look at the data
subplot ( 2, 1, 1 );
plot ( data.Time, data.Speed, [0 max(data.Time)], 5000*[1 1] );
subplot ( 2, 1, 2 );
plot ( data.Time, data.Power );

clear('dev');
disp ( 'Done' );