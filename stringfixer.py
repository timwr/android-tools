#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys
import os
import math
import string
import shutil
import xml.parsers.expat

def testlayout(infile):
    def start_element(name, attrs):
        attrib = attrs.get('android:text')
        if attrib == None:
            continue
        textvalue = str(attrib)
        if '@string' == android_text[0:7]:
            continue
        print textvalue

    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element

    f = open(infile,"r");
    try:
        p.ParseFile(f)
    except:
        return


if __name__ == "__main__":
    for root, subFolders, files in os.walk('res/layout'):
        for ffile in files:
            testfile = os.path.join(root,ffile)
            extension = os.path.splitext(testfile)[1]
            if extension and extension == '.xml':
                testlayout(testfile)

