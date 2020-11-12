from mamba import description, it  # type: ignore
import itertools as itl
from typing import Dict, List, Optional

# https://en.wikipedia.org/wiki/The_Alphabet_Cipher

class Cipher:
    def __init__(self, password):
        x = list( map(chr, range(ord('a'), ord('z')+1)))
        cycled = itl.cycle(x)

        # I captured how I ended up with that specific list comprehension
        # result = [list(itl.islice(cycled, len(x)+1)) for i in x]
        # result2 = [{i: list(itl.islice(cycled, len(x)+1))[:-1]} for i in x]
        # result3 = [{i: dict(zip(x, list(itl.islice(cycled, len(x)+1))[:-1]))} for i in x]
        self.map_table = \
            dict([(i, dict(zip(x, list(itl.islice(cycled, len(x)+1))[:-1]))) for i in x])
        self.password = password


    def encrypt(self, x: str, y: str) -> Optional[str]:
        return self.map_table.get(x, {}).get(y, None)


    def encrypt_word(self, word: str) -> List[Optional[str]]:
        cycled = itl.cycle(self.password)
        base_tuple = list(zip([char for char in word], list(itl.islice(cycled,
            len(word)))))

        return [self.encrypt(x, y) for (x, y) in base_tuple]


with description('Cipher'):

    with it('can create a mapping table'):
        encryptor = Cipher('hello')

        assert encryptor.encrypt('m', 'v') == 'h'
        assert encryptor.encrypt('e', 'i') == 'm'

    with it('can encrypt string with password'):
        encryptor = Cipher('vigilance')
        message = "meetmeontuesdayeveningatseven"

        result = encryptor.encrypt_word(message)
        encrypted_string = "hmkbxebpxpmyllyrxiiqtoltfgzzv"
        assert result == [char for char in encrypted_string]
