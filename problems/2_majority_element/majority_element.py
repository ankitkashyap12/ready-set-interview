# Uses python3
import sys

def get_majority_element(a, left, right):
    """
    Check if array a[left:right] contains an element appearing strictly more than (right - left) // 2 times.
    Approach: Boyer-Moore Voting algorithm + linear verification pass.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if left >= right:
        return -1
    sub = a[left:right]
    if not sub:
        return -1
    
    # Candidate selection
    candidate = None
    count = 0
    for x in sub:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    # Verification pass
    actual_count = sum(1 for x in sub if x == candidate)
    if actual_count > len(sub) // 2:
        return candidate
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
