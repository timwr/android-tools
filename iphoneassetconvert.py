#!/usr/bin/env python

import os
import sys
import string
import shutil
import errno

def copy(fromfile, tofile):
    print 'cp ' + fromfile + ' ' + tofile
    try:
        shutil.copyfile(fromfile, tofile)
    except shutil.Error:
        pass

def createdir(dirname):
    try:
        os.makedirs(dirname)
    except OSError,err:
        if err.errno!=17:
            raise

def copyfile(filename, fullpath):
    global assetpath, outputpath

    if filename.endswith('@2x.png'):
        filename = filename[:-5] + '.png'
    rname = 'ic'
    for i, c in enumerate(filename):
        if c.isupper():
            rname += '_' + string.lower(c)
        else:
            rname += c
    filename = filter(lambda x: x in (string.lowercase + '._'), rname)
    #if filename.endswith('active.png'):
        #filename = filename[:-10] + '_enabled.png'

    dirname = os.path.join(outputpath, 'drawable-xhdpi')
    createdir(dirname)
    outfile = os.path.join(dirname, filename)
    copy(fullpath, outfile)

if __name__ == "__main__":
    global assetpath, outputpath
    assetpath = os.path.abspath('.')
    outputpath = os.path.abspath('.')
    if len(sys.argv) > 1:
        assetpath = sys.argv[1]
        if len(sys.argv) > 2:
            outputpath = sys.argv[2]
    for root, subFolders, files in os.walk(assetpath):
        for ffile in files:
            testfile = os.path.join(root,ffile)
            extension = os.path.splitext(testfile)[1]
            if extension and extension == '.png':
                copyfile(ffile, testfile)

