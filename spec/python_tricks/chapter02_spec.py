from typing import Tuple, Any
from mamba import description, it, context  # type: ignore
from expects import expect, equal, raise_error  # type: ignore
from contextlib import contextmanager
from string import Template


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


with description('Chapter02') as self:
    with context('Asserts'):
        with it("protects the code"):
            shoes = {'name': 'Fancy Shoes', 'price': 14900}
            result = apply_discount(shoes, 0.25)
            expect(result).to(equal(11175))

        with it("will throw assert error for invalid"):
            shoes = {'name': 'Fancy Shoes', 'price': 14900}
            expect(lambda: apply_discount(shoes, 2)).to(
                raise_error(AssertionError))

    with context('with:'):
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

    with context('underscores:'):
        with it("can destructure tuples"):
            car = ('red', 'auto', 12, 3812.4)  # type: Tuple[str, str, int, float]
            color: str
            mileage: float
            _: Any
            color, _, _, mileage = car

            expect(color).to(equal('red'))
            expect(mileage).to(equal(3812.4))

    with context("4 string formattings:"):
        def td(self):  # td = test_data
            return type('', (object,), {
                'errno': 50159747054,
                'name': 'Bob',
                'expected': 'Hello, Bob, there is a 0xbadc0ffee error!',
            })()

        with it("works with old style"):
            # Positional arguments
            positional = 'Hello, %s, there is a 0x%x error!' \
                % (self.td().name, self.td().errno)
            expect(positional).to(equal(self.td().expected))

            # Named arguments, argument order won't matter
            named = 'Hello, %(name)s, there is a 0x%(errno)x error!' \
                % {'name': self.td().name, 'errno': self.td().errno}
            expect(named).to(equal(self.td().expected))

        with it("works with new style - Python3"):
            bob_string = "Hello, {}".format(self.td().name)
            expect(bob_string).to(equal("Hello, Bob"))

            named = 'Hello {name}, there is a 0x{errno:x} error!' \
                    .format(name=self.td().name, errno=self.td().errno)

        with context("literal string interpolation"):
            def greet(self, name, question):
                return f'Hello, {name}! How is it {question}?'

            with it('can embed Python syntax in expressions'):
                expect(f'Hello, {self.td().name}!').to(equal('Hello, Bob!'))

                a = 5
                b = 10
                result = f'Five plus ten is {a + b} and not {2 * (a + b)}.'
                expect(result).to(equal('Five plus ten is 15 and not 30.'))

                # Use:
                # ```python
                # import dis
                # dis.dis(self.greet)
                # ``` - to see the literal implementation.
                expect(self.greet('John', 'going')) \
                    .to(equal('Hello, John! How is it going?'))

        with it("template string"):
            t = Template('Hey, $name!')
            expect(t.substitute(name=self.td().name)) \
                .to(equal('Hey, Bob!'))

            t2 = 'Hello, $name, there is a $error error!'
            result = Template(t2) \
                .substitute(name=self.td().name, error=hex(self.td().errno))

            expect(result).to(equal(self.td().expected))
