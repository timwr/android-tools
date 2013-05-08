#!/usr/bin/env python

import sys
import re
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

logbuf = None

def striptag(line):
    tag = line.find(": ")
    if tag != None:
        print line[tag+2]
        return line[tag+2:]
    return line

def printline(color, line):
    global logbuf
    if len(line) > 3800:
        if logbuf == None:
            logbuf = line
        else:
            logbuf += striptag(line)
    else:
        if logbuf != None: 
            printstring(color, logbuf + striptag(line))
            logbuf = None
        else:
            printstring(color, line)

    
def printstring(color, line):
    if color is None:
        print line
    else:
        print color + line + bcolors.ENDC
        #print str(len(line)) + ']' + color + line + bcolors.ENDC

def outputline(line):
    color = None
    if line[0] == 'E':
        color = bcolors.FAIL
    elif line[0] == 'I':
        color = bcolors.OKGREEN
    elif line[0] == 'W':
        color = bcolors.WARNING
    elif line[0] == 'D':
        color = bcolors.OKBLUE
    printline(color, line)

if __name__ == "__main__":
    grepstring = 'hailo'

    if len(sys.argv) > 1:
        grepstring = sys.argv[1]

    regexes = []

    if grepstring != '-a':
        p = subprocess.Popen(["adb", "shell", "ps"], stdout=subprocess.PIPE)
        stdout = p.communicate()[0]
        for line in stdout.splitlines():
            pstable = line.split()
            if grepstring in pstable[-1]:
                matchstring = '\((\s)*' + pstable[1] + '\):'
                regexes += [re.compile(matchstring)]
                print matchstring

        p = subprocess.Popen(["adb", "logcat"], stdout=subprocess.PIPE)

    while True:
        try:
            line = p.stdout.readline().rstrip()
        except KeyboardInterrupt:
            break

        if len(regexes) > 0:
            for reg in regexes:
                if reg.search(line) != None:
                    outputline(line)
        else:
            outputline(line)



