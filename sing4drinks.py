#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Score   Parts                                 Percentages
# 0.0     oj: 1.0 vodka: 0.0 jägermeister: 1.0  (50% oj,  0% vodka, 50% jägermeister)
# 0.25    oj: 1.5 vodka: 0.5 jägermeister: 0.5  (60% oj, 20% vodka, 20% jägermeister)
# 0.5     oj: 2.0 vodka: 1.0 jägermeister: 0.0  (66% oj, 34% vodka,  0% jägermeister)
# 0.75    oj: 1.5 vodka: 1.0 jägermeister: 0.0  (60% oj, 40% vodka,  0% jägermeister)
# 1.0     oj: 1.0 vodka: 1.0 jägermeister: 0.0  (50% oj, 50% vodka,  0% jägermeister)

import urllib2
from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
     createOSCBundle, sendOSCBundle, startOSCServer

def server():
    initOSCServer("0.0.0.0", 9000, 0)
    setOSCHandler('/drink', drink)
    startOSCServer()
        
def drink(addr, tags, data, source):
    print "score: %s" % data
    score = float(data[0])
    oj, vodka, jag = get_proportions(score, 100)
    parts = []
    if jag:
        parts.append("booze49=%d" % jag)
    if vodka:
        parts.append("booze1=%d" % vodka)
    if oj:
        parts.append("booze4=%d" % oj)
    url = "&".join(parts)

    print "Received %f -> %s" % (score, url)
    urllib2.urlopen("http://bartendro/ws/drink/75?%s" % url)

def get_proportions(score, size):
    if score >= .5:
        vodka = 1
        oj = 3.0 - (score * 2.0)
    else:
        vodka = score * 2
        oj = 1.0 + (score * 2.0)
    jag = 1.0 - vodka

    total = jag + oj + vodka
    oj = int(oj * size / total)
    if oj < 3: oj = 0
    vodka = int(vodka * size / total)
    if vodka < 3: vodka = 0
    jag = int(jag * size / total)
    if jag < 3: jag = 0

    return oj, vodka, jag

if __name__ == '__main__': 
    server()
