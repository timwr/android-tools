#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys
import os
import math
import string
import shutil
import xml.parsers.expat

def testdrawable(infile):
    testdrawable.retvalue = False

    def start_element(name, attrs):
        rcorner = str(attrs.get('android:textSize'))
        if rcorner and rcorner.find('dp') != -1:
            testdrawable.retvalue = True

    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element

    f = open(infile,"r");
    try:
        p.ParseFile(f)
    except:
        return False

    return testdrawable.retvalue

if __name__ == "__main__":
    filelist = []
    for root, subFolders, files in os.walk('res'):
        for ffile in files:
            testfile = os.path.join(root,ffile)
            extension = os.path.splitext(testfile)[1]
            if extension and extension == '.xml':
                filelist.append(testfile)

    #print filelist

    if len(filelist) > 0:
        for ffile in filelist:
            nfile = ffile.replace('.xml', '.tmp')
            print 'Generating: ' + nfile
            newfile = open(nfile, 'w')
            oldfile = open(ffile)
            for line in oldfile:
                templine = line
                if line.find('textSize') != -1:
                    templine = line.replace('sp', 'dp')
                newfile.write(templine)
            newfile.close()
            oldfile.close()
            os.rename(nfile, ffile)
