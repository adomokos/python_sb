import pytest

class TestClass(object):
    def test_list_length(self):
        x = [1,2,3]
        assert len(x) == 3

    def test_with_range(self):
        x = list(range(1,10,2))
        assert x == [1,3,5,7,9]

    def test_slicing(self):
        x = list(range(10))
        sublist = x[3:5]
        sublist == [2,3,4]

    def test_list_append(self):
        x = [1,2,3]
        x.append(5)
        assert x == [1,2,3,5]
        # or
        x += [8,9]
        assert x == [1,2,3,5,8,9]

    def test_list_sort(self):
        x = [5,2,4,1]
        x.sort()
        assert x == [1,2,4,5]

    def test_reverse_list(self):
        x = [5,4,3,2]
        x.reverse()
        assert x == [2,3,4,5]

    def test_item_index(self):
        x = [2,5,10]
        y = x.index(5)
        assert y == 1

    def test_remove_item(self):
        x = [2,8,9,10]
        y = x.remove(8)
        assert y == None
        assert x == [2,9,10]

