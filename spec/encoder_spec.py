from mamba import description, it  # type: ignore
import itertools as itl
from typing import Dict, Optional

# https://en.wikipedia.org/wiki/The_Alphabet_Cipher

x = list( map(chr, range(ord('a'), ord('z')+1)))
cycled = itl.cycle(x)
# result = [list(itl.islice(cycled, len(x)+1)) for i in x]
# result2 = [{i: list(itl.islice(cycled, len(x)+1))[:-1]} for i in x]
# result3 = [{i: dict(zip(x, list(itl.islice(cycled, len(x)+1))[:-1]))} for i in x]
map_table = dict([(i, dict(zip(x, list(itl.islice(cycled, len(x)+1))[:-1]))) for i in x])

def encrypt_values(x: str, y: str, map_table: Dict[str, Dict[str, str]]) -> Optional[str]:
    return map_table.get(x, {}).get(y, None)


with description('Encoder'):
    with it('can create a mapping table'):
        assert len(map_table), 25
        assert encrypt_values('m', 'v', map_table) == 'h'
        assert encrypt_values('e', 'i', map_table) == 'm'

    with it('can encrypt string with password'):
        password = "vigilance"
        message = "meetmeontuesdayeveningatseven"
        cycled = itl.cycle(password)
        base_tuple = list(zip([char for char in message], list(itl.islice(cycled, len(message)))))

        result = [encrypt_values(x, y, map_table) for (x, y) in base_tuple]
        encrypted_string = "hmkbxebpxpmyllyrxiiqtoltfgzzv"
        assert result == [char for char in encrypted_string]
