#!/usr/local/bin/python3
'''
Simple tests to make sure that myUtils changes don't cause any problems.
To run the tests:
    py.test myUtils_test.py

'''

import subprocess

def test_primeFactorization():
    stdout = str(subprocess.check_output('./euler001.py', universal_newlines=True))
    assert 'Result: 233168' in stdout

def test_listOfPrimes():
    solution = {'./euler010.py' : 'Result: 142913828922',\
                './euler035.py' : 'Result: 55',\
                './euler049.py' : 'Result: 296962999629',\
                './euler050.py' : 'Result: 997651'}

    for key, value in solution.items():
        stdout = str(subprocess.check_output(key, universal_newlines=True))
        assert value in stdout


