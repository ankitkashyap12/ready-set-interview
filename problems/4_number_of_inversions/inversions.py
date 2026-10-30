# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    """
    Counts number of inversions in array a using divide-and-conquer (Merge Sort).
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    i, j, k = left, ave, left
    while i < ave and j < right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            number_of_inversions += (ave - i)
            j += 1
        k += 1

    while i < ave:
        b[k] = a[i]
        i += 1
        k += 1

    while j < right:
        b[k] = a[j]
        j += 1
        k += 1

    for idx in range(left, right):
        a[idx] = b[idx]

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
