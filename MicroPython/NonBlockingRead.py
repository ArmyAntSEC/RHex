import sys,uselect

class NonBlockingRead:
    def __init__(self, commandParser ):
        self.spoll=uselect.poll()
        self.spoll.register(sys.stdin,uselect.POLLIN) # type: ignore        
        self.commandParser = commandParser
        self.buffer = ""
    
    def __call__(self):             
        if ( self.spoll.poll(0) ):      
            thisData = str(sys.stdin.read(1))                  
            self.buffer = self.buffer + thisData
            print ( thisData, end='')

            if ( self.buffer[-1] == '\n' ):
                
                # Parse the command                
                self.commandParser ( self.buffer.strip() )

                # Clear the buffer
                self.buffer = ""

            




        
