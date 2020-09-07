from mamba import description, it
from expects import expect, equal, raise_error
from contextlib import contextmanager


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    # Assertions are not expected to signal expected
    # error condition, they are meant to be internal
    # self check
    # The goal of assert is to find the root cause quickly
    assert 0 <= price <= product['price']
    return price


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'r')
        yield f
    finally:
        f.close()


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        return ('    ' * self.level + text)


with description('Asserts') as self:
    with it("protects the code"):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        result = apply_discount(shoes, 0.25)
        expect(result).to(equal(11175))

    with it("will throw assert error for invalid"):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        expect(lambda: apply_discount(shoes, 2)).to(
            raise_error(AssertionError))

    with it("can use/close resources"):
        with ManagedFile('resources/hello.txt') as f:
            result = f.read()
            expect(result).to(equal("Hello, there!\n"))
        with managed_file('resources/hello.txt') as f:
            result = f.read()
            expect(result).to(equal("Hello, there!\n"))

    with it("can use with for indenter - DSL-like"):
        with Indenter() as indent:
            result = indent.print('hi!')
            expect(result).to(equal('    hi!'))
            with indent:
                result = indent.print('hello')
                expect(result).to(equal('        hello'))
