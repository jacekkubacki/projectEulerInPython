#!/usr/bin/env python3
"""Simple tests to make sure that myUtils.py changes don't cause any regressions."""

import unittest
import subprocess
import sys


class MyUtilsTest(unittest.TestCase):

    def runSolutions(self, s):
        for key, value in s.items():
            # TODO: error checking
            stdout = str(subprocess.check_output('python3 ' + key, shell=True, universal_newlines=True))
            assert value in stdout

    def test_arithmeticSum(self):
        solutions = {'euler001.py': 'Result: 233168',
                     'euler023.py': 'Result: 4179871'}
        self.runSolutions(solutions)

    def test_dequote(self):
        solutions = {'euler022.py': 'Result: 871198282',
                     'euler042.py': 'Result: 162'}
        self.runSolutions(solutions)

    def test_isPrime(self):
        solutions = {'euler007.py': 'Result: 104743',
                     'euler027.py': 'Result: -59231',
                     'euler041.py': 'Result: 7652413',
                     'euler058.py': 'Result: 26241'}
        self.runSolutions(solutions)

    def test_listOfDivisors(self):
        solutions = {'euler021.py': 'Result: 31626',
                     'euler023.py': 'Result: 4179871'}
        self.runSolutions(solutions)

    def test_listOfPrimes(self):
        solutions = {'euler010.py': 'Result: 142913828922',
                     'euler027.py': 'Result: -59231',
                     'euler035.py': 'Result: 55',
                     'euler049.py': 'Result: 296962999629',
                     'euler050.py': 'Result: 997651'}
        self.runSolutions(solutions)

    def test_primeFactors(self):
        solutions = {'euler003.py': 'Result: 6857',
                     'euler005.py': 'Result: 232792560',
                     'euler012.py': 'Result: 76576500',
                     'euler023.py': 'Result: 4179871',
                     'euler033.py': 'Result: 100'}
        self.runSolutions(solutions)

    def test_sumOfDigits(self):
        solutions = {'euler016.py': 'Result: 1366',
                     'euler056.py': 'Result: 972',
                     'euler119.py': 'Result: 248155780267521'}
        self.runSolutions(solutions)

    def test_wordValue(self):
        solutions = {'euler022.py': 'Result: 871198282',
                     'euler042.py': 'Result: 162'}
        self.runSolutions(solutions)

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(MyUtilsTest)
    testrunner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    result = testrunner.run(suite)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)
