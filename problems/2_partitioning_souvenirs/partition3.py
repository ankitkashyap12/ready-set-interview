# Uses python3
import sys
import itertools

def partition3(A):
    """
    Determine if array A can be partitioned into 3 subsets with equal sum.
    Target sum for each subset is sum(A) // 3.
    Approach: Dynamic Programming / Memoized DFS with pruning.
    Time Complexity: O(n * (sum/3)^2)
    Space Complexity: O((sum/3)^2)
    """
    total = sum(A)
    if total % 3 != 0 or len(A) < 3:
        return 0
    target = total // 3
    A.sort(reverse=True)
    if A[0] > target:
        return 0

    memo = {}

    def backtrack(idx, s1, s2):
        if idx == len(A):
            return 1 if s1 == target and s2 == target else 0
        state = (idx, s1, s2)
        if state in memo:
            return memo[state]

        # Try placing A[idx] in bucket 1
        if s1 + A[idx] <= target:
            if backtrack(idx + 1, s1 + A[idx], s2):
                memo[state] = 1
                return 1
        # Try placing A[idx] in bucket 2
        if s2 + A[idx] <= target:
            if backtrack(idx + 1, s1, s2 + A[idx]):
                memo[state] = 1
                return 1
        # Try placing A[idx] in bucket 3
        s3 = sum(A[:idx]) - s1 - s2
        if s3 + A[idx] <= target:
            if backtrack(idx + 1, s1, s2):
                memo[state] = 1
                return 1

        memo[state] = 0
        return 0

    return backtrack(0, 0, 0)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

