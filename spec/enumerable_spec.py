from mamba import description, it, description
from itertools import repeat, dropwhile, takewhile


with description('Enumerable') as self:
    with it('can map over a list'):
        x = [1, 2, 3]
        squared = map(lambda x: x*x, x)
        #  print(list(squared))
        assert list(squared) == [1, 4, 9]

    with it('can repeat items'):
        result = repeat(10, 3)
        assert list(result) == [10, 10, 10]

    with it('can dropwhile predicate is true'):
        source = list(range(6))
        result = list(dropwhile(lambda x: x < 4, source))
        assert result == [4, 5]

    with it('can takewhile predicate is true'):
        source = list(range(6))
        result = list(takewhile(lambda x: x < 4, source))
        assert result == [0, 1, 2, 3]
