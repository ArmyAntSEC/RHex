%% Lock and load
clc;
clear;

%% Connect to COM5
port = serialport( 'COM5', 9600, 'Timeout', 2 );
writeline ( port, 'const 3500 0.0003 0.02' )
pause ( 1 )

wantedToken = "#controller";
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
subplot ( 2, 3, 1 );
plot ( data(:,1), data(:,2) )
xlabel ( 'Time [ms]' );
ylabel ( 'Speed [CPS]' );

subplot ( 2, 3, 2 );
plot ( data(:,1), data(:,3) )
xlabel ( 'Time [ms]' );
ylabel ( 'Error [CPS]' );


subplot ( 2, 3, 3 );
plot ( data(:,1), data(:,4) )
xlabel ( 'Time [ms]' );
ylabel ( 'ITerm' );

subplot ( 2, 3, 4 );
plot ( data(:,1), data(:,5) )
xlabel ( 'Time [ms]' );
ylabel ( 'Power [0-1]' );

subplot ( 2, 3, 5 );
plot ( data(:,1), data(:,6) )
xlabel ( 'Time [ms]' );
ylabel ( 'Position' );