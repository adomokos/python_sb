from mamba import description, it, context  # type: ignore
from expects import expect, equal, raise_error  # type: ignore
from typing import List, Type
import copy
import math


class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


def validate(name: str):
    if len(name) < 5:
        raise NameTooShortError(name)
    if len(name) > 10:
        raise NameTooLongError(name)


class Pizza:
    def __init__(self: 'Pizza', radius: int, ingredients: List[str]):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self: 'Pizza') -> str:
        return f'Pizza({self.ingredients!r})'

    def get_ingredients(self: 'Pizza') -> List[str]:
        return self.ingredients

    def area(self: 'Pizza') -> float:
        return self.circle_area(self.radius)

    @classmethod
    def margherita(cls: Type['Pizza']) -> 'Pizza':
        return cls(4, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls: Type['Pizza']) -> 'Pizza':
        return cls(5, ['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r: int) -> float:
        return r ** 2 * math.pi


with description('Chapter04') as self:
    with context('custom errors'):
        with it("will signal better errors"):
            expect(lambda: validate('joe')).to(
                raise_error(NameTooShortError))
            expect(lambda: validate('mysuperlongnamejoe')).to(
                raise_error(NameTooLongError))

    with context('cloning objects'):
        with it('shallow copy'):
            xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            ys = list(xs)  # make a shallow copy
            expect(len(xs)).to(equal(len(ys)))

            xs.append([3, 7, 9])
            # Adding an item to the first will not add to the second
            expect(len(xs)).to(equal(len(ys) + 1))

            # But modifying copied items will update both
            xs[1][0] = 9
            expect(xs[1][0]).to(equal(ys[1][0]))

        with it('deep copy'):
            xs = [[1, 2, 3], [4, 5, 6]]
            zs = copy.deepcopy(xs)
            expect(len(xs)).to(equal(len(zs)))

            # Modify one element, it's unchanged in the other
            xs[1][0] = 9
            assert xs[1][0] == 9
            assert zs[1][0] == 4

    with context('class and static methods'):
        with it('can have different roles'):
            p = Pizza.margherita()
            expect(p.ingredients).to(equal(['mozzarella', 'tomatoes']))
            assert p.area() > 0
