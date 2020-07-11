import asyncio
import random
import time
import inspect

# Info from here: https://docs.python.org/3/library/asyncio-task.html


async def main1():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# Run coroutines concurrenctly as asyncio Tasks
async def main3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds).
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# Awaitable - can be used in an `await` expression


async def nested():
    return 42


async def main4():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*
    # nested() - even throws an error

    # Let's do it differently now and await it:
    print(await nested())  # will print 42


# Examples from here - https://realpython.com/async-io-python/
# Gather will collect calculation results


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def runner():
    await asyncio.gather(count(), count(), count())


def main5():
    s = time.perf_counter()
    asyncio.run(runner())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# Chaining coroutines
# A key feature of coroutines is that they can be chained together.

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    duration = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {duration:0.2f} seconds.)")


async def chain_runner(*args):
    await asyncio.gather(*(chain(n) for n in args))


def main6():
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(chain_runner(*args))
    duration = time.perf_counter() - start
    print(f"Program finished in {duration:0.2f} seconds.")


# A simple calculator example


async def numberA() -> int:
    await asyncio.sleep(3)
    return 3


async def numberB() -> int:
    await asyncio.sleep(3)
    return 4


async def main() -> None:
    start = time.perf_counter()

    [a, b] = await asyncio.gather(numberA(), numberB())

    duration = time.perf_counter() - start

    print(
        f"Adding {a} and {b} together will produce: {a + b} and took {duration: 0.2f}")


def run():
    print(inspect.iscoroutinefunction(main))
    asyncio.run(main())  # in case the main function is async
    #  main()
