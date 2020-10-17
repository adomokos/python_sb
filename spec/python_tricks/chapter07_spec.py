from mamba import description, it, context  # type: ignore
# from expects import expect, raise_error  # type: ignore

from typing import Dict

name_for_userid: Dict[int, str] = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


def greeting(userid: int) -> str:
    return 'Hi %s!' % name_for_userid.get(userid, 'there')


with description('Chapter07') as self:
    with context('dictionary'):
        with it('can return a default value if key not found'):
            assert greeting(382) == 'Hi Alice!'
            assert greeting(383) == 'Hi there!'

        with it('can be sorted'):
            xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
            result = sorted(xs.items())

            assert [*map(lambda x: x[0], result)] \
                == ['a', 'b', 'c', 'd']
