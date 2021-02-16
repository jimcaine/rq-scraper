import os
import unittest
from rq_scraper import __module_path__

def run_unit_tests():
    """
    Runs all unit tests in the tests/unit directory.
    """

    # resolve path to unit test dir
    test_dir = os.path.join(__module_path__, 'tests', 'unit')

    # load tests to suite
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir, '*.py')

    # create runner and run
    runner = unittest.TextTestRunner()
    results = runner.run(suite)

    # parse and return results as dict
    results = { 'wasSuccessful' : results.wasSuccessful() }

    # log
    print('Unit tests complete: {}'.format(results))

    return results

if __name__ == '__main__':
    run_unit_tests()
