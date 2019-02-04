import pytest
from collections import Counter

class TestClass(object):
    def colors(self):
        return ['blue','red','blue','yellow','blue','red']

    def test_counter_functionality(self):
        assert len(self.colors()) == 6
        counter = Counter(self.colors())
        assert counter == Counter({'blue':3,'red':2,'yellow':1})
        assert counter.most_common()[0][0] == 'blue'

