#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys
import os
import math
import string
import shutil
import xml.parsers.expat

def get_var_name(instring):
    var_name = ''
    words = instring.split(' ')
    for word in words:
        var_name += word.lower() + '_'
    return var_name[:-1]

def testlayout(infile):
    def start_element(name, attrs):
        attrib = attrs.get('android:text')
        if attrib == None:
            return
        textvalue = str(attrib)
        if '@string' == textvalue[0:7]:
            return
        var_name = get_var_name(textvalue)
        print '<string name="' + var_name + '">' + textvalue + '</string>'

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

