from mamba import description, it


with description('A list') as self:
    with it("can tell its length"):
        x = [1, 2, 3]
        assert len(x) == 3

    with it('can be build from range'):
        x = list(range(1, 10, 2))
        assert x == [1, 3, 5, 7, 9]

    with it('can slice a list'):
        x = list(range(10))
        sub_list = x[3:5]
        assert sub_list == [3, 4]

    with it('can be appended'):
        x = [1, 2, 3]
        x.append(5)
        assert x == [1, 2, 3, 5]
        x += [8, 9]
        assert x == [1, 2, 3, 5, 8, 9]  # Kinda like assert

    with it('can be sorted'):
        x = [5, 2, 4, 1]
        x.sort()
        assert x == [1, 2, 4, 5]

    with it('can be reversed'):
        x = [5, 4, 3, 2]
        x.reverse()
        assert x == [2, 3, 4, 5]

    with it('can item tell its index'):
        x = [2, 5, 10]
        y = x.index(5)
        assert y == 1

    with it('can remove an item'):
        x = [2, 8, 9, 10]
        y = x.remove(8)
        assert x == [2, 9, 10]
