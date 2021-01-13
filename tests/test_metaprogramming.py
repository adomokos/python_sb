from typing_extensions import TypedDict


class Test:pass

Test.x = 5  # type: ignore

Test.foo = lambda self: self.x + 3  # type: ignore


def test_method(self=None):
    return 5


class Base:
    def my_fun(self):
        return 6


Test2 = type("Test2", (Base, ), dict(x="atul", my_method=test_method))

Movie = TypedDict("Movie", {"name": str, "year": int})
Writer = TypedDict("Writer", {"name": str, "age": int})


class Atdict(dict):
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__  # type: ignore
    __delattr__= dict.__delitem__  # type: ignore


def test_metaclass():
    myObj = Test()
    assert myObj.x == 5
    assert myObj.foo() == 8


def test_class_with_dict():
    myObj = Test2()
    assert myObj.my_fun() == 6
    assert myObj.my_method() == 5
    assert myObj.x == "atul"


def test_typed_dict():
    movie = {"name": "Blade Runner", "year": 1982}
    assert movie["name"] == "Blade Runner"


def test_field_access():
    at_dict = Atdict({"one": 1, "two": "T"})
    assert at_dict.one == 1
    at_dict.one = "1"
    assert at_dict.one == "1"


def test_merge_dictionaries():
    x = {"name": str, "year": int}
    y = {"name": str, "age": int}

    combined = {**x, **y}
    Context = TypedDict("Context", combined, total=True)
    c = Context()
    c["name"] = 23

    assert c["name"] == 23
