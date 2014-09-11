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
    

def test_primeFactors():
    solutions = {'euler003.py' : 'Result: 6857',\
                 'euler005.py' : 'Result: 232792560',\
                 'euler012.py' : 'Result: 76576500'}
    runSolutions(solutions)

def test_listOfPrimes():
    solutions = {'euler010.py' : 'Result: 142913828922',\
                 'euler027.py' : 'Result: -59231',\
                 'euler035.py' : 'Result: 55',\
                 'euler049.py' : 'Result: 296962999629',\
                 'euler050.py' : 'Result: 997651'}
    runSolutions(solutions)
    
def test_dequote():
    solutions = {'euler022.py' : 'Result: 871198282',\
                 'euler042.py' : 'Result: 162'}
    runSolutions(solutions)

def test_wordValue():
    solutions = {'euler022.py' : 'Result: 871198282',\
                 'euler042.py' : 'Result: 162'}
    runSolutions(solutions)
    
def test_sumOfDigits():
    solutions = {'euler016.py' : 'Result: 1366',\
                 'euler056.py' : 'Result: 972',\
                 'euler119.py' : 'Result: 248155780267521'}
    runSolutions(solutions)

def test_isPrime():
    solutions = {'euler007.py' : 'Result: 104743',\
                 'euler027.py' : 'Result: -59231',\
                 'euler041.py' : 'Result: 7652413'}
    runSolutions(solutions)
