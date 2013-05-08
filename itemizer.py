#!/usr/bin/env python

import sys

outdata = ''

def printitem(inputstring):
    global outdata
    inputstring = inputstring.strip()
    name = inputstring[:inputstring.find("=")]
    item = inputstring[inputstring.find('"')+1:-1]
    outdata += '<item name="' + name + '">' + item + '</item>\n'

for line in iter(sys.stdin.readline, ""): 
    if (len(line) < 2):
        print outdata
        outdata = ''
    else:
        printitem(line)

