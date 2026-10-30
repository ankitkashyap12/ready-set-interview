# Uses python3
import sys

def binary_search(a, x):
    """
    Search for x in sorted array a.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Returns: 0-based index of x if present, else -1.
    """
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)
    data = list(map(int, input_data))
    n = data[0]
    a = data[1 : n + 1]
    m = data[n + 1]
    queries = data[n + 2 : n + 2 + m]
    results = [binary_search(a, x) for x in queries]
    print(' '.join(map(str, results)))
