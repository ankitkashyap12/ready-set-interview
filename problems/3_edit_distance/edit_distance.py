# Uses python3
def edit_distance(s, t):
    """
    Compute Levenshtein distance (min insertions, deletions, substitutions) between strings s and t.
    Time Complexity: O(|s| * |t|)
    Space Complexity: O(|t|) using two DP rows
    """
    m, n = len(s), len(t)
    dp = list(range(n + 1))

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[j] = min(
                dp[j] + 1,        # deletion
                dp[j - 1] + 1,    # insertion
                prev + cost       # substitution or match
            )
            prev = temp

    return dp[n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
