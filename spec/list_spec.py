from mamba import description, it
from expects import expect, equal


with description('A list') as self:
    with it("can tell its length"):
        x = [1, 2, 3]
        expect(len(x)).to(equal(3))

    with it('can be build from range'):
        x = list(range(1, 10, 2))
        expect(x).to(equal([1, 3, 5, 7, 9]))

    with it('can slice a list'):
        x = list(range(10))
        sub_list = x[3:5]
        expect(sub_list).to(equal([3, 4]))

    with it('can be appended'):
        x = [1, 2, 3]
        x.append(5)
        expect(x).to(equal([1, 2, 3, 5]))
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
