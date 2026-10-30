# Uses python3
import sys

def optimal_weight(W, w):
    """
    0-1 Knapsack without repetition where each item's value equals its weight.
    Find maximum weight subset of bars that fits into knapsack of capacity W.
    Time Complexity: O(n * W)
    Space Complexity: O(W) with 1D DP rolling array
    """
    dp = [0] * (W + 1)
    for weight in w:
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + weight)
    return dp[W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
