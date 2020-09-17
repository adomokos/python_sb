from mamba import description, it, context  # type: ignore
from typing import Callable
from expects import expect, equal  # type: ignore
from functools import wraps


def yell(text: str) -> str:
    return text.upper() + '!'


def greet(func: Callable) -> str:
    greeting = func('Hi, I am a Python program')
    return greeting


with description('Chapter03') as self:
    with context('functions'):
        with it("first class citizens"):
            result = yell('hello')
            expect(result).to(equal('HELLO!'))

        with it("can be aliased"):
            bark = yell
            result = bark('hello')
            expect(result).to(equal('HELLO!'))

        with it("name is attached to function"):
            bark = yell
            result = bark.__name__
            expect(result).to(equal('yell'))

        with it("can be stored in list"):
            funcs = [yell, str.lower, str.capitalize]
            expect(len(funcs)).to(equal(3))

            result = [f('Hey') for f in funcs]
            assert result == ['HEY!', 'hey', 'Hey']

            assert funcs[0]('Hey') == 'HEY!'

        with it("can be passed to other functions"):
            result = greet(yell)
            assert result == 'HI, I AM A PYTHON PROGRAM!'

        with it("can be nested"):
            def speak(text: str) -> str:
                def whisper(t):
                    return t.lower() + '...'
                return whisper(text)

            result = speak("Hello, World")
            expect(result).to(equal('hello, world...'))

            def get_speak_func(volume: float) -> Callable:
                def whisper(text: str) -> str:
                    return text.lower() + '...'

                def yell(text: str) -> str:
                    return text.upper() + '!'

                if volume > 0.5:
                    return yell
                else:
                    return whisper

            result2 = get_speak_func(0.3)
            assert result2('Hey') == 'hey...'
            result3 = get_speak_func(0.7)
            assert result3('Hey') == 'HEY!'

        with it("can capture local state"):
            def get_speak_func(text: str, volume: float) -> Callable[[], str]:
                def whisper() -> str:
                    return text.lower() + '...'

                def yell() -> str:
                    return text.upper() + '!'

                if volume > 0.5:
                    return yell
                else:
                    return whisper

            result = get_speak_func('Hey', 0.4)
            assert result() == 'hey...'

            def make_adder(n: int) -> Callable:
                def add(x: int) -> int:
                    return x + n
                return add

            plus_3 = make_adder(3)
            plus_5 = make_adder(5)

            assert plus_3(4) == 7
            assert plus_5(4) == 9

        with it("objects can behave like functions"):
            class Adder:
                def __init__(self, n):
                    self.n = n

                def __call__(self, x):
                    return self.n + x

            plus_3 = Adder(3)
            assert plus_3(4) == 7

            assert callable(plus_3)
            assert callable(yell)
            assert not callable('hello')

    with context('lambdas'):
        with it("single-expression functions"):
            result = (lambda x, y: x + y)(5, 3)
            assert result == 8

        with it("useful lambdas"):
            tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
            result = sorted(tuples, key=lambda x: x[1])
            assert result == [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

            result = sorted(range(-5, 6), key=lambda x: x * x)
            assert result == [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

            def make_adder(n: int) -> Callable:
                return lambda x: x + n

            plus_3 = make_adder(3)
            plus_5 = make_adder(5)
            assert plus_3(4) == 7
            assert plus_5(4) == 9

    with context('decorators'):
        with it('functions can decorate other fns'):
            def null_decorator(func: Callable) -> Callable:
                return func

            def greet() -> str:
                return 'Hello!'

            greet = null_decorator(greet)
            result = greet()
            assert result == 'Hello!'

            @null_decorator
            def greet2():
                return 'Hello!'

            assert greet2() == 'Hello!'

        with it('decorators can modify behavior'):
            def uppercase(func):
                def wrapper():
                    original_result = func()
                    modified_result = original_result.upper()
                    return modified_result
                return wrapper

            @uppercase
            def greet():
                return 'Hello!'

            result = greet()
            assert result == 'HELLO!'

            def strong(func):
                def wrapper():
                    return '<strong>' + func() + '</strong>'
                return wrapper

            def emphasis(func):
                def wrapper():
                    return '<em>' + func() + '</em>'
                return wrapper

            @strong
            @emphasis
            def greet():
                return 'Hello!'

            result = greet()
            assert result == '<strong><em>Hello!</em></strong>'

        with it('can forward arguments'):
            def trace(func):
                def wrapper(*args, **kwargs):
                    original_args = f'TRACE: calling {func.__name__}() - '\
                                     f'with {args}, {kwargs}'
                    result = func(*args, **kwargs)
                    output = f'TRACE: {func.__name__}() ' \
                             f'returned {result!r}'
                    return original_args + result + output
                return wrapper

            @trace
            def say(name, line):
                return f'{name}: {line}'

            result = say('Jane', 'Hello, World')
            assert result.startswith("TRACE: calling say()")

        with it('use functools.wrap for copying metadata'):
            def uppercase(func):
                @wraps(func)
                def wrapper():
                    return func().upper()
                return wrapper

            @uppercase
            def greet():
                """Return a friendly greeting."""
                return 'Hello!'

            result = greet()
            assert result == 'HELLO!'

            func_name = greet.__name__
            assert func_name == 'greet'

            doc = greet.__doc__
            assert doc == 'Return a friendly greeting.'

    with context('function argument unpacking'):
        with it('can help simplifying the code'):
            def vector_tos(x: int, y: int, z: int) -> str:
                return ('<%s, %s, %s>' % (x, y, z))

            expected = '<1, 0, 1>'
            result = vector_tos(1, 0, 1)
            assert result == expected

            tuple_vec = (1, 0, 1)
            list_vec = [1, 0, 1]
            assert vector_tos(*tuple_vec) == expected
            assert vector_tos(*list_vec) == expected

            genexpr = (x * x for x in range(3))
            expect(vector_tos(*genexpr)).to(equal('<0, 1, 4>'))
