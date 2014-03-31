#!/usr/bin/env python

import sys
import string

outdata = ''

def printitem(inputstring):
    global outdata
    name = inputstring.replace(' ', '_').upper()
    outdata += 'public static final String ' + name + ' = "' + inputstring + '"\n'

for line in iter(sys.stdin.readline, ""): 
    if (len(line) < 2):
        print outdata
        outdata = ''
    else:
        printitem(line.rstrip('\n'))

