from mamba import description, it


released = {
    "iphone": 2007,
    "iphone 3G": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4S": 2011,
    "iphone 5": 2012
}

with description('Dictionary'):
    with it('can get the keys'):
        keys = released.keys()
        assert len(keys) == 6

    with it('can get the values'):
        values = released.values()
        assert len(values) == 6
        assert list(values)[0] == 2007

    with it('can get the default if not found'):
        item = released.get('iphone', 0)
        assert item == 2007
        item = released.get('iphone1', 0)
        assert item == 0

    with it('can be initialized with list of fields'):
        items = [['one', 1], ['two', 2], ['three', 3]]
        d = dict(items)
        assert len(d.keys()) == 3

    with it('can remove item from dictionary'):
        value = released.pop('iphone')
        assert value == 2007
        assert len(released) == 5
