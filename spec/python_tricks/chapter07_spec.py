from mamba import description, it, context  # type: ignore
# from expects import expect, raise_error  # type: ignore

import operator
from typing import Dict

name_for_userid: Dict[int, str] = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}


def greeting(userid: int) -> str:
    return 'Hi %s!' % name_for_userid.get(userid, 'there')


with description('Chapter07') as self:
    with context('dictionary'):
        with it('can return a default value if key not found'):
            assert greeting(382) == 'Hi Alice!'
            assert greeting(383) == 'Hi there!'

        with it('can be sorted'):
            result = sorted(xs.items())
            assert [*map(lambda x: x[0], result)] \
                == ['a', 'b', 'c', 'd']

        with it('can be sorted by values'):
            result = sorted(xs.items(), key=lambda x: x[1])
            assert [*map(lambda x: x[0], result)] \
                == ['d', 'c', 'b', 'a']

            result2 = sorted(xs.items(), key=operator.itemgetter(1))
            assert [*map(lambda x: x[0], result2)] \
                == ['d', 'c', 'b', 'a']

            result3 = sorted(xs.items(), key=lambda x: x[1], reverse=True)
            assert [*map(lambda x: x[0], result3)] \
                == ['a', 'b', 'c', 'd']

        with it("merge dictionaries"):
            xs = {'a': 1, 'b': 2}
            ys = {'b': 3, 'c': 4}

            zs = {**xs, **ys}

            assert zs == {'a': 1, 'b': 3, 'c': 4}
