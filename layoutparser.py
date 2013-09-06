#!/usr/bin/env python

# parse an xml layout and produce android code to access the elements with ids

import sys
import xml.parsers.expat

privates = str()
lookups = str()

if len(sys.argv) < 2:
    print "Usage " , sys.argv[0] , " layout.xml";
else:
    adapter = False
    private = True
    view = ''
    if len(sys.argv) > 2:
        if sys.argv[2] == 'adapter':
            view = 'convertView.'
            adapter = True
        else:
            view = sys.argv[2] + '.'
            if len(sys.argv) > 3:
                private = False

    def start_element(name, attrs):
        global privates
        global lookups

        if 'android:id' in attrs:
            classname = str(name)
            if classname == 'include' or classname == 'merge':
                classname = 'View'
            rid = str(attrs.get('android:id'))
            rid = rid[rid.find('/')+1:]
            rname = 'm' + classname
            addname = ''
            foundunderscore = False
            for i, c in enumerate(rid):
                if c == '_':
                    if i == 0:
                        return
                    foundunderscore = True
                    i += 1
                elif foundunderscore:
                    addname += c.upper()
                    foundunderscore = False
                elif len(addname) > 0:
                    addname += c
            rname = rname + addname

            privates += '' if adapter else 'private ' 
            privates += classname + ' ' +  rname + ';\n'
            lookups += 'holder.' if adapter else '' 
            if not private:
                lookups += classname + ' '
            lookups += rname + ' = (' + classname + ') '
            lookups += view
            lookups += 'findViewById(R.id.' + rid + ');\n'
            if classname == 'Button':
                lookups += 'holder.' if adapter else '' 
                lookups += rname + '.setOnClickListener(new View.OnClickListener() {\n'
                lookups += '\t@Override\n'
                lookups += '\tpublic void onClick(View v) {\n'
                lookups += '\t\t' + rname + 'Clicked();\n'
                lookups += '\t}\n'
                lookups += '});\n'

            #print 'Start element:', name, "attrs:", attrs
            #print 'rid', rid
            #print 'rname', rname


    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element

    f = open(sys.argv[1],"r");
    p.ParseFile(f)

    if private:
        print privates
    print lookups
