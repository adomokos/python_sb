from mamba import description, it


with description('List Comprehension'):
    with it('can create a list'):
        numbers = [i for i in range(5)]
        assert numbers == [0, 1, 2, 3, 4]

    with it('can square all its elements'):
        x = [i*2 for i in range(5) if i % 2 == 0]
        assert x == [0, 4, 8]
