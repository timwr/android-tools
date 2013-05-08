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
        if name != 'corners':
            return

        rcorner = str(attrs.get('android:bottomRightRadius'))
        lcorner = str(attrs.get('android:bottomLeftRadius'))

        if rcorner != lcorner:
            #print 'Start element:', name, "attrs:", attrs
            testdrawable.retvalue = True

    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element

    f = open(infile,"r");
    try:
        p.ParseFile(f)
    except:
        return False

    if testdrawable.retvalue:
        infile

    return testdrawable.retvalue

if __name__ == "__main__":
    filelist = []
    for root, subFolders, files in os.walk('res/drawable'):
        for ffile in files:
            testfile = os.path.join(root,ffile)
            extension = os.path.splitext(testfile)[1]
            if extension and extension == '.xml':
                if testdrawable(testfile):
                    filelist.append(testfile)

    #print filelist

    if len(filelist) > 0:
        if not os.path.exists('res/drawable-v12'):
            os.makedirs('res/drawable-v12')
        
        for ffile in filelist:
            nfile = ffile.replace('/drawable/', '/drawable-v12/')
            print 'Generating: ' + nfile
            newfile = open(nfile, 'w')
            oldfile = open(ffile)
            for line in oldfile:
                templine = line.replace('bottomRightRadius', 'bottomTempRadius')
                templine = templine.replace('bottomLeftRadius', 'bottomRightRadius')
                templine = templine.replace('bottomTempRadius', 'bottomLeftRadius')
                newfile.write(templine)
            newfile.close()
            oldfile.close()
