# Uses python3
import sys

def optimal_sequence(n):
    """
    Find minimal sequence of operations (+1, *2, *3) to reach n from 1.
    Greedy fails (e.g. 10 -> 9 -> 3 -> 1 takes 3 ops, while 10 -> 5 -> 4 -> 2 -> 1 takes 4 ops).
    Approach: Dynamic Programming with path reconstruction.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return [1]

    # dp[i] stores min operations to reach i from 1
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    # Reconstruct path from n down to 1
    curr = n
    path = []
    while curr >= 1:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
