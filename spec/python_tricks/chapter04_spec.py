from mamba import description, it, fit, context  # type: ignore
from expects import expect, equal, raise_error  # type: ignore
import copy


class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 5:
        raise NameTooShortError(name)
    if len(name) > 10:
        raise NameTooLongError(name)


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

        with fit('deep copy'):
            xs = [[1, 2, 3], [4, 5, 6]]
            zs = copy.deepcopy(xs)
            expect(len(xs)).to(equal(len(zs)))

            # Modify one element, it's unchanged in the other
            xs[1][0] = 9
            assert xs[1][0] == 9
            assert zs[1][0] == 4
