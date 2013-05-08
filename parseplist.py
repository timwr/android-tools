#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import plistlib
import xml.parsers.expat

DESIRED_PADDING = 30

config = {}

def printconfig_xml():
    for c in config:
        spaceavailable = DESIRED_PADDING - len(testxml.keyname)
        if spaceavailable > 0:
            tabs = '\t' * (spaceavailable / 4)
        else:
            tabs = ' '
        print '\t<' + c + tabs + 'value="' + config[c] + '"/>'

def printconfig():
    print config
    #print json.dumps(config)

def testxml():
    config = plistlib.readPlist(sys.argv[1])
    printconfig()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage " , sys.argv[0] , " input.plist";
    else:
        testxml()


