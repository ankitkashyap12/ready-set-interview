# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, op, m, M):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], op[k])
        b = evalt(M[i][k], m[k + 1][j], op[k])
        c = evalt(m[i][k], M[k + 1][j], op[k])
        d = evalt(m[i][k], m[k + 1][j], op[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    """
    Finds maximum value of an arithmetic expression by placing parentheses.
    Dynamic programming over subexpression lengths.
    Time Complexity: O(n^3) where n is the number of digits.
    Space Complexity: O(n^2)
    """
    digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    ops = [dataset[i] for i in range(1, len(dataset), 2)]
    n = len(digits)

    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, ops, m, M)

    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
