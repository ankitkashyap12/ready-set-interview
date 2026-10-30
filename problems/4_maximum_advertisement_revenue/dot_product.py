#Uses python3

import sys

def max_dot_product(a, b):
    """
    Maximizes advertisement revenue by sorting click values and ad slots (Rearrangement Inequality).
    Time Complexity: O(n log n)
    Space Complexity: O(1) beyond sorting
    """
    a.sort()
    b.sort()
    return sum(x * y for x, y in zip(a, b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
