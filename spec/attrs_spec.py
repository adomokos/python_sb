from mamba import description, it
from attr import attrs, attrib
import attr
import typing


@attr.s
class Empty(object):
    pass


@attr.s
class Coordinates(object):
    x = attr.ib()
    y = attr.ib()


@attrs
class SeriousCoordinates(object):
    x = attrib()
    y = attrib()

# Subclassing is bad for you...
@attr.s
class A(object):
    a = attr.ib()

    def get_a(self):
        return self.a


@attr.s
class B(object):
    b = attr.ib()


@attr.s
class C(A, B):
    c = attr.ib()


@attr.s
class SomeClass(object):
    a_number = attr.ib(default=42)
    list_of_numbers = attr.ib(factory=list)

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number

# asdict can accept a lambda
@attr.s
class UserList(object):
    users = attr.ib()


@attr.s
class User(object):
    email = attr.ib()
    password = attr.ib()


@attr.s(auto_attribs=True)
class AnotherClass:
    a_number: int = 42
    list_of_numbers: typing.List[int] = attr.Factory(list)


with description('Attrs') as self:
    with it("works with Empty objects"):
        empty1 = Empty()
        empty2 = Empty()
        assert empty1 == empty2
        assert (empty1 is empty2) is False

    with it("works with coordinates"):
        c1 = Coordinates(x=2, y=1)
        c2 = Coordinates(x=2, y=1)
        assert c1 == c2
        c3 = Coordinates(1, 2)
        assert (c2 != c3)

    with it("works with SeriousCoordinates"):
        a = Coordinates(1, 2)
        b = SeriousCoordinates(1, 2)
        assert attr.fields(Coordinates) == attr.fields(SeriousCoordinates)

    with it("works with inheritance"):
        i = C(1, 2, 3)
        assert i == C(1, 2, 3)

    with it("can have various attributes, even lists"):
        sc = SomeClass(1, [1, 2, 3])
        assert sc.hard_math(3) == 19
        assert sc == SomeClass(1, [1, 2, 3])

    with it("can convert to dictionaries"):
        d1 = attr.asdict(Coordinates(x=1, y=2))
        assert [*d1.keys()] == ['x', 'y']

    with it("asdict can accept lambda to filter"):
        user_list = UserList(
            [User("jane@doe.invalid", "s33kred"),
             User("joe@doe.invalid", "p4ssw0rd")]
        )
        d1 = attr.asdict(
            user_list,
            filter=lambda attr, value: attr.name != "password"
        )
        assert len(d1['users']) == 2

    with it("can use typing as well"):
        sc = SomeClass(1, [1, 2, 3])
        assert sc.list_of_numbers == [1, 2, 3]
