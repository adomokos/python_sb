import pytest

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

class TestClass(object):
    def test_factorial_with_recursion(self):
        result = fact(5)
        assert result == 120
