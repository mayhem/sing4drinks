#!/usr/bin/env python

import sys
from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
     createOSCBundle, sendOSCBundle, startOSCServer

initOSCClient("localhost", 9000)
sendOSCMsg("/drink", [sys.argv[1]]) 
