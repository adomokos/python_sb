from mamba import description, it, context  # type: ignore
from expects import expect, raise_error  # type: ignore


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


with description('Chapter06') as self:
    with context('comprehension'):
        with it('works with lists'):
            even_squares = [x * x for x in range(10) if x % 2 == 0]
            assert even_squares == [0, 4, 16, 36, 64]

        with it('works with sets'):
            s = {x * x for x in range(1, 4)}
            assert s == {1, 4, 9}

        with it('works with dict'):
            d = {x: x * x for x in range(1, 4)}
            assert d == {1: 1, 2: 4, 3: 9}

    with context('slicing'):
        with it('works like this: lst[start:end:step]'):
            lst = range(1, 6)
            assert list(lst[1:3:1]) == [2, 3]

        with it('step defaults to one'):
            lst = range(1, 6)
            assert list(lst[1:3]) == [2, 3]

        with it('can create a list with steps'):
            lst = range(1, 6)
            assert list(lst[::2]) == [1, 3, 5]

        with it('can reverse a list'):
            lst = range(1, 6)
            assert list(lst[::-1]) == [5, 4, 3, 2, 1]

        with it('can clear a list'):
            lst2 = [1, 2, 3, 4, 5]
            del lst2[:]
            assert lst2 == []

    with context('iterators'):
        with it('needs __iter__ and __next__ dunders'):
            repeater = Repeater('Hello')
            iterator = iter(repeater)
            assert next(iterator) == 'Hello'
            assert next(iterator) == 'Hello'

        with it('works from list'):
            my_list = [1, 2, 3]
            list_iterator = iter(my_list)
            assert next(list_iterator) == 1
            assert next(list_iterator) == 2
            assert next(list_iterator) == 3

            expect(lambda: next(list_iterator)).to(
                raise_error(StopIteration))
