# Uses python3
import sys

def get_change(m):
    """
    Minimum coins to change m using denominations 1, 3, 4.
    Greedy fails (e.g. 6 = 3 + 3, not 4 + 1 + 1), so Dynamic Programming is used.
    Time Complexity: O(m)
    Space Complexity: O(m)
    """
    if m <= 0:
        return 0
    coins = [1, 3, 4]
    dp = [0] + [float('inf')] * m
    for i in range(1, m + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
