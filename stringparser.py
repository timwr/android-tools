#!/usr/bin/env python

import sys
import os
import math
import string
import shutil
import xml.parsers.expat

#import codecs, locale

#if sys.stdout.encoding is None:
    #(lang, enc) = locale.getdefaultlocale()
    #if enc is not None:
        #(e, d, sr, sw) = codecs.lookup(enc)
        #sys.stdout = sw(sys.stdout)

def testxml(infile):
    testxml.name = None

    def start_element(name, attrs):
        #print 'element:', name, "attrs:", attrs
        if name == 'string':
            testxml.name = str(attrs.get('name'))
            sys.stdout.write(testxml.name + '=')

    def end_element(name):
        if testxml.name != None:
            sys.stdout.write('\n')
        testxml.name = None
        #print 'end element:', name

    def string_data(text):
        if testxml.name != None:
            sys.stdout.write(text.encode('utf8'))

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

