%% Lock and load
clc;
clear;

%% Connect to COM5
port = serialport( 'COM5', 9600, 'Timeout', 1 );
pause ( 1 )

wantedToken = "#beacon";
data = [];
line = readline ( port ); 
for ii = 1:50
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
plot ( data(2:end,1), diff(data(:,1)), '.-' )
xlabel ( 'Time [ms]' );
ylabel ( 'Time Delta' );