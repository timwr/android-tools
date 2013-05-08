#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys
import os
import math
import string
import shutil
import xml.parsers.expat

def testxml(infile):
    testxml.printvalue = False

    def start_element(name, attrs):
        print 'element:', name, "attrs:", attrs
        if name == 'string':
            testxml.printvalue = True

    def end_element(name):
        testxml.printvalue = False
        print 'end element:', name

    def string_data(text):
        if testxml.printvalue:
            print "DATA", text

    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element
    p.EndElementHandler = end_element
    p.CharacterDataHandler = string_data

    f = open(infile,"r");
    try:
        p.ParseFile(f)
    except:
        raise
        return False


    return True

if __name__ == "__main__":
    filelist = []
    for root, subFolders, files in os.walk('res/values'):
        for ffile in files:
            testfile = os.path.join(root,ffile)
            extension = os.path.splitext(testfile)[1]
            if extension and extension == '.xml':
                testxml(testfile)

