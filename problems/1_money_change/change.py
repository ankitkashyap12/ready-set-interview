# Uses python3
import sys

def get_change(m):
    """
    Greedy change using coin denominations 10, 5, 1.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    tens = m // 10
    remainder = m % 10
    fives = remainder // 5
    ones = remainder % 5
    return tens + fives + ones

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
