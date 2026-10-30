# Uses python3
import sys

def optimal_summands(n):
    """
    Represents n as a sum of the maximum number of pairwise distinct positive integers.
    Greedy strategy: greedily allocate 1, 2, 3... until remaining value <= 2 * current.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(sqrt(n))
    """
    summands = []
    k = 1
    while n > 2 * k:
        summands.append(k)
        n -= k
        k += 1
    summands.append(n)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
