#!/usr/bin/env python

import sys
import string
from xml.sax.saxutils import escape

def printitem(inputstring):
    global outdata
    name = inputstring.replace(' ', '_').lower()
    name = filter(lambda x: x in (string.lowercase + '_'), name)
    if len(inputstring) == 0:
        return
    if inputstring[0] == ' ':
        inputstring = '"' + inputstring + '"'
    
    print '<string name="' + name + '">' + escape(inputstring) + '</string>'

while True:
    line = sys.stdin.readline()
    if line != None:
        printitem(line.rstrip('\n'))

