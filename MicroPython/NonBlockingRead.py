import sys,uselect

class NonBlockingRead:
    def __init__(self, commandParser ):
        self.spoll=uselect.poll()
        self.spoll.register(sys.stdin,uselect.POLLIN) # type: ignore        
        self.commandParser = commandParser
        self.buffer = ""
    
    def __call__(self):             
        if ( self.spoll.poll(0) ):                        
            self.buffer = self.buffer + str(sys.stdin.read(1))                        
            if ( self.buffer[-1] == '\n' ):
                
                # Parse the command
                print ( "Running command: ", self.buffer.strip() )
                self.commandParser ( self.buffer.strip() )

                # Clear the buffer
                self.buffer = ""

            




        
