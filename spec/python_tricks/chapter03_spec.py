from mamba import description, it, context, fit
from expects import expect, equal, raise_error


def yell(text):
    return text.upper() + '!'


with description('Chapter03') as self:
    with context('functions'):
        with it("first class citizens"):
            result = yell('hello')
            expect(result).to(equal('HELLO!'))
