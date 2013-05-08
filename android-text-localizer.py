#!/usr/bin/env python

"""
Usage: ./android-text-localizer.py <android layout file> <strings xml file>

Recommended you install python-lxml, but this script should still work with
nearly any Python installation.

IMO, one of the most annoying things about Android is its insistence that
developers localize strings by referencing the strings in layouts using @string
and placing the actual string in res/values/strings.xml.

This script does that for you automatically. It will parse a layout file for
any element with an android:text attribute. If that attribute has not already
been localized, it generates the correct <string> element and writes it to the
strings XML file. It will also re-write the layout file to use the new <string>
element.

The name of the string is the android:id of the element it came from. If the
element doesn't have an android:id, a random string is used. If the name is
duplicated in the strings.xml, a random string is appended.

Errors and warnings are printed at the end of processing.

Author: Joman Chu <github@notatypewriter.com>
License: Public domain / Apache License 2.0
"""

import string
import random
import sys

# Compatibility code stolen from http://lxml.de/tutorial.html
try:
  from lxml import etree as ElementTree
  #print >> sys.stderr, "running with lxml.etree"
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as ElementTree
    #print >> sys.stderr, "running with cElementTree on Python 2.5+"
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as ElementTree
      #print >> sys.stderr, "running with ElementTree on Python 2.5+"
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as ElementTree
        #print >> sys.stderr, "running with cElementTree"
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as ElementTree
          #print >> sys.stderr, "running with ElementTree"
        except ImportError:
          print >> sys.stderr, "Failed to import ElementTree from any known place"
          sys.exit(2)

def gen_rand_str(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
  """
  Generates a random string, defaulting to length 10.
  Stolen from http://stackoverflow.com/a/2257449
  """
  return ''.join(random.choice(chars) for x in range(size))

# Check and set arguments
if (len(sys.argv) < 3):
  print >> sys.stderr, 'Usage: %s <android layout file> <strings xml file>' % (sys.argv[0])
  sys.exit(1)

LAYOUTFILE = sys.argv[1]
STRINGSFILE = sys.argv[2]

errors = []

# Parse xml files
layout_tree = ElementTree.parse(LAYOUTFILE)
strings_tree = ElementTree.parse(STRINGSFILE)
nsmap = layout_tree.getroot().nsmap
prefix = '{%s}' % nsmap['android']

#print >> sys.stderr, ElementTree.tostring(layout_tree)
#print >> sys.stderr, layout_tree.getroot().nsmap

r = layout_tree.xpath('//*[@android:text]', namespaces=nsmap)
#print >> sys.stderr, r
for elem in r:
  #print >> sys.stderr, elem.attrib

  android_text = elem.get(prefix+'text')
  #print >> sys.stderr, android_text

  # Skip if already localized
  if '@string' == android_text[0:7]:
    continue;

  # Get an id
  android_id = elem.get(prefix+'id')
  if android_id != None and '@+id/' == android_id[0:5]:
    android_id = android_id.split('/',1)[1]
  else:
    android_id = gen_rand_str(size=4)
    errors.append('WARN: Unable to find id for element %s at %s. ' \
        'Random string \"%s\" used for name'
        % (elem.tag, layout_tree.getpath(elem), android_id))
    #continue

  # De-duplicate name in strings.xml
  original_android_id = android_id
  while True:
    localized = strings_tree.xpath('//string[@name=\"%s\"]' % (android_id)) 
    if len(localized) <= 0:
      if android_id != original_android_id:
        errors.append('WARN: Duplicated string name \"%s\" at %s. ' \
            'Used name \"%s\" instead.'
            % (original_android_id, layout_tree.getpath(elem), android_id))
      break
    android_id = android_id + gen_rand_str(size=1, chars=string.digits)

  # Generate <string>
  stringElem = ElementTree.Element("string")
  stringElem.set('name', android_id)
  stringElem.text = android_text
  #print ElementTree.tostring(stringElem)
  strings_tree.getroot().insert(len(strings_tree.getroot()), stringElem)

  # Set element to refer to <string>
  elem.set(prefix+'text', '@string/'+android_id)

# Write files
file = open(STRINGSFILE, 'w')
strings_tree.write(file, pretty_print=True)
file.close()

file = open(LAYOUTFILE, 'w')
layout_tree.write(file, pretty_print=True)
file.close()

# Print errors
if len(errors) > 0:
  print >> sys.stderr, ''
for e in errors:
  print >> sys.stderr, e
