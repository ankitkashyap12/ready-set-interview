#Uses python3

import sys

from functools import cmp_to_key

def largest_number(a):
    """
    Composes the largest number from a collection of integers.
    Custom comparator: a comes before b if a + b > b + a.
    Time Complexity: O(n log n * L) where L is max number of digits.
    Space Complexity: O(n)
    """
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        return 0

    sorted_a = sorted(a, key=cmp_to_key(compare))
    if sorted_a and sorted_a[0] == '0':
        return '0'
    return "".join(sorted_a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
