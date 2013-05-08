#!/usr/bin/env python

# quick simple script to detect unused resources
# install python (brew install python)
# delete the drawable-mdpi/ldpi folders to avoid outputting duplicated resources

import os
import sys
import math
import string

from subprocess import call

print "The build succeeds without:"

for root, subFolders, files in os.walk('res'):
    for file in files:
        testfile = os.path.join(root,file)

        call("rm " + testfile, stdout=open(os.devnull, 'wb'), shell=True)

        call("ant clean", stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'), shell=True)
        return_code = call("ant debug", stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'), shell=True)
        if return_code == 0:
            print testfile

        call("git checkout -- " + testfile, stdout=open(os.devnull, 'wb'), shell=True)
