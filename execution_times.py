#!/usr/local/bin/python3
"""
Sorts the scripts by execution time to find candidates for optimization.
Returns 0 if each script finishes within TIME_LIMIT seconds, returns 1 otherwise.
"""

# TODO:
# - nice pattern matching when parsing stderr
# - TIME_LIMIT could be a script parameter

import glob
import sys
import subprocess
import re

TIME_LIMIT = 10  # in seconds
FILE_PATTERN = "euler*.py"

results = []
exit_code = 0

listOfFiles = glob.glob(FILE_PATTERN)
print ("%d file%s found." % (len(listOfFiles), "s"[len(listOfFiles)==1:]), file=sys.stderr)

for f in listOfFiles:
    print (".", end="", flush=True, file=sys.stderr)  # progress indicator
    
    executeString = 'time ' + 'python3 ' + f
    cmd = subprocess.Popen(executeString, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    '''
    sample output:
    real    0m1.590s
    user    0m1.560s
    sys     0m0.025s
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

            if realTime >= TIME_LIMIT * 1000:
                # set return code to 1
                exit_code = 1
            
            results.append({'fileAndTime' : f + '\t' + timeString,  'realTime' : realTime})
            # no need to parse other lines
            break

print ("", end="\n", flush=True, file=sys.stderr)  # new line

for r in sorted(results, key=lambda k: k['realTime'], reverse=True):
    print (r['fileAndTime'])

sys.exit(exit_code)
