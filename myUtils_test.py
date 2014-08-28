#!/usr/local/bin/python3
'''
Simple tests to make sure that myUtils changes don't cause any problems.
To run the tests:
    py.test myUtils_test.py
'''

import subprocess

def test_primeFactorization():
    solution = {'euler005.py' : 'Result: 232792560',\
                'euler012.py' : 'Result: 76576500'}

    for key, value in solution.items():
        stdout = str(subprocess.check_output('python3 ' + key, shell = True, universal_newlines=True))
        assert value in stdout

    
    stdout = str(subprocess.check_output('python3 euler005.py', shell=True, universal_newlines=True))
    assert 'Result: 232792560' in stdout

def test_listOfPrimes():
    solution = {'euler010.py' : 'Result: 142913828922',\
                'euler035.py' : 'Result: 55',\
                'euler049.py' : 'Result: 296962999629',\
                'euler050.py' : 'Result: 997651'}

    for key, value in solution.items():
        stdout = str(subprocess.check_output('python3 ' + key, shell = True, universal_newlines=True))
        assert value in stdout
