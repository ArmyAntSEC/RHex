%% Lock and load
clc;
clear;

%% Connect to COM5
port = serialport( 'COM5', 9600);
writeline ( port, 'const' )
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
%%
plot ( data(:,1), data(:,4) )
xlabel ( 'Time [ms]' );
ylabel ( 'Power [0-1]' );