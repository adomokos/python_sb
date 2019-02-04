import pytest

released = { "iphone":2007
           , "iphone 3G":2008
           , "iphone 3GS":2009
           , "iphone 4":2010
           , "iphone 4S":2011
           , "iphone 5":2012
           }

# In case I need to skip a tes
#  pytest.skip("not yet implemented")
class TestClass(object):
    def test_keys_in_dictionary(self):
        keys = released.keys()
        assert len(keys) == 6

    def test_values_in_dictionary(self):
        vals = released.values()
        assert len(vals) == 6

    def test_get_with_default_if_no_found(self):
        item = released.get("iphone", 0)
        assert item == 2007
        item = released.get("iphone1", 0)
        assert item == 0

    def test_initialize_dict_with_list_of_list(self):
        items = [["one",1],["two",2],["three",3]]
        d = dict(items)
        assert len(d.keys()) == 3

    def test_remove_item_from_dict(self):
        value = released.pop("iphone")
        assert value == 2007
        assert len(released) == 5

