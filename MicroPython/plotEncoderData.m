%% Lock and load
clc;
clear;

%% Connect to COM5
port = serialport( 'COM5', 9600, 'Timeout', 1 );
writeline ( port, 'move' )
pause ( 1 )

wantedToken = "#encoder";
data = [];
line = readline ( port ); 
while ( numel(line) > 0 )    
    tokens = split( line, {'(', ')', ',', ' '} );            
    if ( tokens(1) == wantedToken )
        numTokens = (numel(tokens)-2)/2;
        tokenIdx = 1+(1:numTokens)*2;
        tokens = tokens(tokenIdx);
        data = [data; str2double( tokens )']; %#ok
    end    
    line = readline ( port );
end

disp ( data );
clear port 
%% Preprocess the data
data(:,1) = data(:,1) - min( data(:,1) );

%%
subplot ( 3, 1, 1 );
plot ( data(:,1), data(:,2), '.-' )
xlabel ( 'Time [ms]' );
ylabel ( 'Speed [CPS]' );

subplot ( 3, 1, 2 );
plot ( data(:,1), data(:,3), '.-' )
xlabel ( 'Time [ms]' );
ylabel ( 'Position' );

subplot ( 3, 1, 3 );
plot ( data(:,1), data(:,4), '.-' )
xlabel ( 'Time [ms]' );
ylabel ( 'Time Delta' );