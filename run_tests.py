import unittest
'''
the file in /tests/homework/
has the test functions
'''
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)