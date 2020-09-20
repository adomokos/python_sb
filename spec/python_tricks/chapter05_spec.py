from mamba import description, it, context  # type: ignore
from expects import expect, equal, raise_error  # type: ignore
from collections import OrderedDict, ChainMap, namedtuple
from typing import Dict, List
from types import MappingProxyType
import array


class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


with description('Chapter05') as self:
    with context('dicts'):
        with it('fast lookup'):
            phonebook: Dict[str, int] = {
                'bob': 7387,
                'alice': 3719,
                'jack': 7052,
                }
            assert phonebook['alice'] == 3719

            squares = {x: x * x for x in range(6)}
            assert len(squares.keys()) == 6

    with context('ordered dict'):
        with it('keeps keys in order'):
            d = OrderedDict(one=1, two=2, three=3)
            assert d['two'] == 2
            d['four'] = 4
            assert list(d.keys()) == ['one', 'two', 'three', 'four']

    with context('ChainMap'):
        with it('searches multiple dictionaries'):
            dict1: Dict[str, int] = {'one': 1, 'two': 2}
            dict2: Dict[str, int] = {'three': 3, 'four': 4}
            chain = ChainMap(dict1, dict2)
            assert chain['three'] == 3
            assert chain['one'] == 1

    with context('MappingProxyType'):
        with it('is a read-only dictionary'):
            writable = {'one': 1, 'two': 2}
            read_only = MappingProxyType(writable)
            assert read_only['one'] == 1

            def set_item(x):
                read_only['two'] = x

            expect(lambda: set_item(42)).to(
                raise_error(TypeError))

    with context('Lists'):
        with it('is mutable'):
            arr: List[str] = ['one', 'two', 'three']
            assert len(arr) == 3

            arr[1] = 'hello'
            assert arr == ['one', 'hello', 'three']

            del arr[1]
            assert arr == ['one', 'three']

            arr.append('ok')
            assert arr == ['one', 'three', 'ok']

    with context('tuples'):
        with it('is immutable containers'):
            arr2 = 'one', 'two', 'three'
            assert arr2[1] == 'two'
            assert len(arr2) == 3

            def remove_item():
                del arr2[1]

            expect(lambda: remove_item()).to(
                raise_error(TypeError)
            )

    with context('array'):
        with it('is mutable'):
            arr3 = array.array('f', (1.0, 1.5, 2.0, 2.5))
            assert arr3[1] == 1.5
            del arr3[1]
            assert len(arr3) == 3
            arr3.append(42.0)
            assert list(arr3) == [1.0, 2.0, 2.5, 42.0]

    with context('strings'):
        with it('stores textual data as immutable sequences'):
            arr4 = 'abcd'
            assert arr4[1] == 'b'

            def change_char(c):
                arr4[1] = c

            expect(lambda: change_char('x')).to(
                raise_error(TypeError))

            assert list(arr4) == ['a', 'b', 'c', 'd']

    with context('bytes'):
        with it('immutable arrays of single bytes'):
            arr5 = bytes((0, 1, 2, 3,))

            def add_byte(b):
                bytes((0, 300))

            expect(lambda: add_byte(300)).to(
                raise_error(ValueError))

    with context('bytearray'):
        with it('is mutable'):
            arr6 = bytearray((0, 1, 2, 3))
            arr6[1] = 23

            assert len(arr6) == 4
            assert arr6[1] == 23

    with context('custom class'):
        with it('comes more control'):
            car1 = Car('red', 3812.4, True)
            car2 = Car('blue', 40231.0, False)

            # classes are mutable
            car2.mileage = 12

            assert car2.mileage == 12

    with context('namedtuples'):
        with it('is immutable data structure'):
            Point = namedtuple('Point', ['x', 'y', 'z'])
            p1 = Point(1, 2, 3)

            assert p1.x == 1

            Car2 = namedtuple('Car2', ['color', 'mileage', 'automatic'])
            car3 = Car2('red', 3812.4, True)

            assert car3.color == 'red'

            def assign_windshield(ws):
                car3.windshield = ws

            # Can't assign attribute that does not exist
            expect(lambda: assign_windshield('broken')).to(
                raise_error(AttributeError))

    with context('sets'):
        with it('is unordered data structure with no duplicate values'):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            assert 'e' in vowels

            letters = set('alice')
            assert letters.intersection(vowels) == {'a', 'e', 'i'}

            assert len(vowels) == 5
            vowels.add('x')
            assert len(vowels) == 6

    with context('frozenset'):
        with it('is immutable'):
            vowels2 = frozenset({'a', 'e', 'i', 'o', 'u'})

            def add_vowel(c):
                vowels2.add(c)

            expect(lambda: add_vowel('x')).to(
                raise_error(AttributeError))
