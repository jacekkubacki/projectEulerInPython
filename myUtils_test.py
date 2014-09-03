#!/usr/local/bin/python3
'''
Simple tests to make sure that myUtils changes don't cause any problems.
To run the tests:
    py.test myUtils_test.py
'''

import subprocess

def runSolutions (s):
    for key, value in s.items():
        stdout = str(subprocess.check_output('python3 ' + key, shell = True, universal_newlines=True))
        assert value in stdout
    

def test_primeFactorization():
    solutions = {'euler005.py' : 'Result: 232792560',\
                 'euler012.py' : 'Result: 76576500'}
    runSolutions(solutions)

def test_listOfPrimes():
    solutions = {'euler010.py' : 'Result: 142913828922',\
                 'euler035.py' : 'Result: 55',\
                 'euler049.py' : 'Result: 296962999629',\
                 'euler050.py' : 'Result: 997651'}
    runSolutions(solutions)
    
def test_dequote():
    solutions = {'euler042.py' : 'Result: 162'}
    runSolutions(solutions)

def test_wordValue():
    solutions = {'euler042.py' : 'Result: 162'}
    runSolutions(solutions)
    
def test_sumOfDigits():
    solutions = {'euler016.py' : 'Result: 1366',\
                 'euler056.py' : 'Result: 972'}
    runSolutions(solutions)
    