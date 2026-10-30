# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    """
    Fractional Knapsack greedy algorithm.
    Sort items by value-per-unit-weight descending.
    Take maximal fraction until capacity is filled.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    value = 0.0
    items = sorted(
        [(v, w, v / w) for v, w in zip(values, weights) if w > 0],
        key=lambda x: x[2],
        reverse=True
    )
    for v, w, unit_val in items:
        if capacity <= 0:
            break
        take_weight = min(capacity, w)
        value += take_weight * unit_val
        capacity -= take_weight

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
