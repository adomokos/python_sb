from mamba import description, it, context  # type: ignore
# from expects import expect, raise_error  # type: ignore


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
