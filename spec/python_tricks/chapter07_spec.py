from mamba import description, it, context  # type: ignore
# from expects import expect, raise_error  # type: ignore

from typing import Dict

name_for_userid: Dict[int, str] = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

with description('Chapter07') as self:
    with context('dictionary'):
        with it('can return a default value if key not found'):
            assert 2 > 1
