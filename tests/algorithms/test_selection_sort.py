import pytest

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

class TestClass(object):
    def test_counter_functionality(self):
        my_list = [5,3,4,2,7,1]
        assert selection_sort(my_list) == [1,2,3,4,5,7]
