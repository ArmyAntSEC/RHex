import sys,uselect

class NonBlockingRead:
    def __init__(self):
        self.spoll=uselect.poll()
        self.spoll.register(sys.stdin,uselect.POLLIN) # type: ignore        
        self.buffer = ""
    
    def __call__(self):             
        if ( self.spoll.poll(0) ):                        
            self.buffer = self.buffer + str(sys.stdin.read(1))
            print ( ":> " + self.buffer ) 



        
