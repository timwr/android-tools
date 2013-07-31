#!/usr/bin/env python

import sys

checkable = False
bitmap = False
inputdata = sys.argv

if len(inputdata) < 2:
    inputdata = sys.stdin.readline().split()
elif len(inputdata) > 2:
    if any('checkable' == s.lower() for s in inputdata):
        checkable = True
    if any('bitmap' == s.lower() for s in inputdata):
        bitmap = True
    inputdata = inputdata[1:]
else:
    inputdata = inputdata[1:]

if len(inputdata) < 1:
    print "Usage " , sys.argv[0] , " drawable (e.g icon_blah[.png])"

drawable = inputdata[0]
newfile = open(drawable + '.xml', 'w')
newfile.write( '<?xml version="1.0" encoding="utf-8"?>\n')
newfile.write( '<selector xmlns:android="http://schemas.android.com/apk/res/android">\n')
if bitmap:
    newfile.write( '<item android:state_pressed="true"><bitmap android:gravity="center" android:src="@drawable/' + drawable + '_pressed"/></item>\n')
    if checkable:
        newfile.write( '<item android:state_checked="true"><bitmap android:gravity="center" android:src="@drawable/' + drawable + '_selected"/></item>\n')
    newfile.write( '<item><bitmap android:gravity="center" android:src="@drawable/' + drawable + '_normal"/></item>\n')
else:
    newfile.write( '<item android:state_pressed="true" android:drawable="@drawable/' + drawable + '_pressed"/>\n')
    if checkable:
        newfile.write( '<item android:state_checked="true" android:drawable="@drawable/' + drawable + '_selected"/>\n')
    newfile.write( '<item android:drawable="@drawable/' + drawable + '_normal"/>\n')
newfile.write( '</selector>\n')
newfile.close()

