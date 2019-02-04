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

    def test_dog(self):
        d = python_sb.Dog('Fido')
        assert d.name == 'Fido'
        d.add_trick('roll over')
        assert len(d.tricks) == 1
        assert d.tricks.__len__() == 1


#  class BasicTestSuite(unittest.TestCase):
    #  """Basic test cases."""

    #  def test_absolute_truth_and_meaning(self):
        #  assert True


#  if __name__ == '__main__':
    #  unittest.main()
