#!/usr/bin/env python

import sys

inputdata = sys.argv

if len(inputdata) < 2:
    inputdata = sys.stdin.readline().split()
else:
    inputdata = inputdata[1:]

if len(inputdata) < 1:
    print "Usage " , sys.argv[0] , " drawable (e.g icon_blah[.png])"

drawable = inputdata[0]
newfile = open(drawable + '.xml', 'w')
newfile.write( '<?xml version="1.0" encoding="utf-8"?>\n')
newfile.write( '<selector xmlns:android="http://schemas.android.com/apk/res/android">\n')
newfile.write( '<item android:state_pressed="true" android:drawable="@drawable/' + drawable + '_pressed"/>\n')
newfile.write( '<item android:drawable="@drawable/' + drawable + '_default"/>\n')
newfile.write( '</selector>\n')
newfile.close()

