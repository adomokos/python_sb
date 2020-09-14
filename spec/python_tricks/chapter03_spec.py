from mamba import description, it, context, fit
from expects import expect, equal


def yell(text):
    return text.upper() + '!'


def greet(func):
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
            def speak(text):
                def whisper(t):
                    return t.lower() + '...'
                return whisper(text)

            result = speak("Hello, World")
            expect(result).to(equal('hello, world...'))

            def get_speak_func(volume):
                def whisper(text):
                    return text.lower() + '...'

                def yell(text):
                    return text.upper() + '!'
                if volume > 0.5:
                    return yell
                else:
                    return whisper

            result = get_speak_func(0.3)
            assert result('Hey') == 'hey...'
            result = get_speak_func(0.7)
            assert result('Hey') == 'HEY!'

        with it("can capture local state"):
            def get_speak_func(text, volume):
                def whisper():
                    return text.lower() + '...'

                def yell():
                    return text.upper() + '!'
                if volume > 0.5:
                    return yell
                else:
                    return whisper

            result = get_speak_func('Hey', 0.4)
            assert result() == 'hey...'

            def make_adder(n):
                def add(x):
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
