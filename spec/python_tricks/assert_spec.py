from mamba import description, fit
from expects import expect, equal


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


with description('Asserts') as self:
    with fit("protects the code"):
        shoes = {'name': 'Fancy Shoes', 'price': 14900}
        result = apply_discount(shoes, 0.25)
        expect(result).to(equal(11175))
