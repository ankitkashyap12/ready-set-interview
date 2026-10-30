def majority_wins(arr, n, x, y):
    """
    Find which element (x or y) appears most frequently in arr.
    If frequency is equal, return the smaller element.
    Time Complexity: O(n)
    Auxiliary Space: O(1)
    """
    count_x = 0
    count_y = 0

    for val in arr[:n]:
        if val == x:
            count_x += 1
        elif val == y:
            count_y += 1

    if count_x > count_y:
        return x
    elif count_y > count_x:
        return y
    return min(x, y)

if __name__ == '__main__':
    print(majority_wins([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], 11, 4, 5))  # 4
    print(majority_wins([1, 2, 3, 4, 5, 6, 7, 8], 8, 1, 7))             # 1
