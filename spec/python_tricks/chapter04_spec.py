from mamba import description, it, context  # type: ignore
from expects import expect, raise_error  # type: ignore


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
