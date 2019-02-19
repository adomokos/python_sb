import pytest

# Logarithms
# log(10) 100 = 2
#
# For algorithms, log always means log(2) - log = logarithms
# With binary search, with a list of 8 elements,
# log(2) 8 = 3, we would need to check 3 times to find the
# element. For a list of 1024 elements, log(2) 1024 = 10,
# we would have to check 10 numbers at most.

# *Running time*
# Checking 4 billion items one by one takes 4 billion guesses.
# That's linear time.
# However, with binary search, it takes only 32 guesses. Binary
# search runs in logarithmic time.

#  Simple Search     | Binary Search
#  ------------------------------------
#  100 items         | 100 items
#  100 guesses       | 7 guesses
#  ------------------------------------
#  4 billion items   | 4 billion items
#  4 billion guesses | 32 guesses (Big Savings)
#  ------------------------------------
#  O(n)              | O(log n)

#  Big O establishes wort-case run time
#  O (log n) - log time - example: binary search
#  O (n) - linear time - example: simple search
#  O (n*log n) - fast sorting algorithm - like quicksort
#  O (n^2) - slow sorting algorithm - like selection sort
#  O (n!) - a really slow algorithm - like the traveling salesperson

def binary_search (list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

class TestClass(object):
    def test_counter_functionality(self):
        my_list = [1,3,5,7,9]
        assert binary_search(my_list, 7) == 3
        assert binary_search(my_list, 8) == None
