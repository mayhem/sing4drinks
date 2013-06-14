#!/usr/bin/env python

from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
     createOSCBundle, sendOSCBundle, startOSCServer

def myTest():
    """ a simple function that creates the necesary sockets and enters an enless
        loop sending and receiving OSC
    """
    import time # in this example we will have a small delay in the while loop
    
    initOSCClient("37.34.68.87", 3333) # takes args : ip, port
    try:
        while 1:
            for i in xrange(100):
                sendOSCMsg("/score", ["%.2f" % (i / 100.0)]) 
                time.sleep(0.01)

    except KeyboardInterrupt:
       closeOSC() # finally close the connection before exiting or program.
  

if __name__ == '__main__': myTest()

