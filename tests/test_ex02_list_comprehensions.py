import pytest

class TestClass(object):
    def test_list_comprehension(self):
        numbers = [i for i in range(5)]
        assert numbers == [0,1,2,3,4]
        x = [i*2 for i in range(5) if i % 2 == 0]
        assert x == [0,4,8]
