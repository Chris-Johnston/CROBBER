import unittest
import doctest
import post
import sys

test_modules = [
    post
]

def load(tests):
    for m in test_modules:
        tests.addTests(doctest.DocTestSuite(m))
    return tests

if __name__ == "__main__":
    """
    Runs the tests
    """
    tests = unittest.TestSuite()
    test = load(tests)
    run = unittest.TextTestRunner()
    ret = not run.run(tests).wasSuccessful()
    sys.exit(ret)