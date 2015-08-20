#!/usr/local/bin/python3
"""Run 'time' utility and sort the results to find candidates for optimization."""

# ToDo:
# - nice pattern matching when parsing stderr


import glob
import sys
import subprocess
import re

results = []

listOfFiles = glob.glob('euler*.py')
print ("%d file%s found." % (len(listOfFiles), "s"[len(listOfFiles)==1:]), file=sys.stderr)

for file in listOfFiles:
    print (".", end="", flush=True, file=sys.stderr)  # progress indicator
    
    executeString = 'time ' + 'python3 ' + file
    cmd = subprocess.Popen(executeString, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    '''
    sample output:
    real	0m1.590s
    user	0m1.560s
    sys	    0m0.025s
    '''
    for line in cmd.stderr:
        if "real" in line:
            # line.split() sample result: ['real', '0m1.590s']
            timeString = line.split()[1]
            
            # re.split() with r"\D+" sample result: ['', '0', '1', '564', '']
            timeInt = [int(i) for i in re.split(r"\D+", timeString) if len(i) > 0] 
            assert len(timeInt) == 3
            
            # convert minutes and seconds to thousandths
            realTime = 60*1000*timeInt[0] + 1000*timeInt[1] + timeInt[2]
            
            results.append({'fileAndTime' : file + '\t' + timeString,  'realTime' : realTime})
            # no need to parse other lines
            break

print ("", end="\n", flush=True, file=sys.stderr)  # new line

for r in sorted(results, key=lambda k: k['realTime'], reverse=True):
    print (r['fileAndTime'])
