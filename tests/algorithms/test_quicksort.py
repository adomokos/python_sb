import pytest

def sum(xs):
    if xs == []:
        return 0
    else:
        head, *tail = xs
        return head + sum(tail)

def count(xs):
    if xs == []:
        return 0
    else:
        head, *tail = xs
        return 1 + count(tail)

def quicksort(xs):
    if len(xs) < 2:
        return xs
    else:
        pivot = xs[0]
        less = [i for i in xs[1:] if i <= pivot]
        greater = [i for i in xs[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


class TestClass(object):
    def test_sum(self):
        result = sum([])
        assert result == 0
        result = sum([1,2,3])
        assert result == 6

    def test_count(self):
        result = count([])
        assert result == 0
        result = count([1,2,3,4])
        assert result == 4

    def test_quicksort(self):
        result = quicksort([3,4,1,2])
        assert result == [1,2,3,4]
