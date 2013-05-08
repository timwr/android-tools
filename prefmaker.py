#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys

inputdata = sys.argv

if len(inputdata) < 3:
    inputdata = sys.stdin.readline().split()
else:
    inputdata = inputdata[1:]

if len(inputdata) < 2:
    print "Usage " , sys.argv[0] , " type name (e.g long pref)"

datatype = inputdata[0]
dataftype = datatype[:1].upper() + datatype[1:]
dataname = inputdata[1].lower()
if len(inputdata) > 2:
    for word in inputdata[2:]:
        dataname += '_' + word.lower()
dataconst = inputdata[1].upper()
if len(inputdata) > 2:
    for word in inputdata[2:]:
        dataconst += '_' + word.upper()
datafname = ''
for word in inputdata[1:]:
    datafname += word[:1].upper() + word[1:]

if datatype == 'boolean':
    datadefault = 'false'
elif datatype == 'String':
    datadefault = '""'
else:
    datadefault = '0'

print '\tprivate final static String ' + dataconst + ' = "' + dataname + '_key";'
print ''
print '\tpublic ' + datatype + ' get' + datafname + '() {'
print '\t\treturn preferences.get' + dataftype + '(' + dataconst + ', ' + datadefault + ');'
print '\t}'
print ''
print '\tpublic void set' + datafname + '(' + datatype + ' ' + dataname + ') {'
print '\t\tpreferencesEditor.put' + dataftype + '(' + dataconst + ', ' + dataname + ').commit();'
print '\t}'


