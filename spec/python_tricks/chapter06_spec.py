from mamba import description, it, context  # type: ignore
from expects import expect, raise_error  # type: ignore


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
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

        with it('works with bounds'):
            repeater2 = BoundedRepeater('Hello', 3)
            result = list(map(lambda x: x.upper(), repeater2))
            assert result == ['HELLO', 'HELLO', 'HELLO'], result

    with context('generators'):
        with it('repeat it three times'):
            def repeat_three_times(value):
                yield value
                yield value
                yield value

            iterator3 = repeat_three_times('Hey!')
            assert next(iterator3) == 'Hey!'
            assert next(iterator3) == 'Hey!'
            assert next(iterator3) == 'Hey!'

            expect(lambda: next(iterator3)).to(
                raise_error(StopIteration))

            expect(lambda: next(iterator3)).to(
                raise_error(StopIteration))

        with it('can be bounded as well'):
            def bounded_repeater(value, max_repeats):
                count = 0
                while True:
                    if count >= max_repeats:
                        return
                    count += 1
                    yield value

            result4 = map(lambda x: x.upper(), bounded_repeater('Hi', 4))
            assert list(result4) == ['HI', 'HI', 'HI', 'HI']

    with context('generator expressions'):
        with it('is a single line expression'):
            iterator_sl = ('Hello' for i in range(3))

            assert next(iterator_sl) == 'Hello'
            assert next(iterator_sl) == 'Hello'
            assert next(iterator_sl) == 'Hello'

            expect(lambda: next(iterator_sl)).to(
                raise_error(StopIteration))

        with it('expression can be concise'):
            assert sum((x * 2 for x in range(10))) == 90
            # The parens are not needed
            assert sum(x * 2 for x in range(10)) == 90

    with context('generator chains'):
        with it('can be chained together'):
            def integers():
                for i in range(1, 9):
                    yield i

            def squared(seq):
                for i in seq:
                    yield i * i

            chain = squared(integers())
            assert list(chain) == [1, 4, 9, 16, 25, 36, 49, 64]

            integers2 = range(8)
            squared2 = (i * i for i in integers2)
            negated = (-i for i in squared2)

            assert list(negated) == [0, -1, -4, -9, -16, -25, -36, -49]
