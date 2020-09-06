from mamba import description, it, fit
from expects import expect, equal, raise_error


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    # Assertions are not expected to signal expected
    # error condition, they are meant to be internal
    # self check
    # The goal of assert is to find the root cause quickly
    assert 0 <= price <= product['price']
    return price


with description('Asserts') as self:
    with it("protects the code"):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        result = apply_discount(shoes, 0.25)
        expect(result).to(equal(11175))

    with it("will throw assert error for invalid"):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        expect(lambda: apply_discount(shoes, 2)).to(
            raise_error(AssertionError))
