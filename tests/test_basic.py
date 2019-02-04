# -*- coding: utf-8 -*-

from .context import python_sb

import pytest

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = python_sb.get_hmm()
        assert x == 'hmmm...'



#  class BasicTestSuite(unittest.TestCase):
    #  """Basic test cases."""

    #  def test_absolute_truth_and_meaning(self):
        #  assert True


#  if __name__ == '__main__':
    #  unittest.main()
