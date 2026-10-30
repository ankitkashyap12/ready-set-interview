# python3
import sys


def compute_min_refills(distance, tank, stops):
    """
    Greedy car fueling: always advance to the furthest reachable gas station before refilling.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # All stops including origin (0) and destination (distance)
    all_stops = [0] + list(stops) + [distance]
    num_refills = 0
    current_idx = 0
    n = len(all_stops) - 2 # number of intermediate stations

    while current_idx <= n:
        last_idx = current_idx
        # Greedily drive as far as possible
        while current_idx <= n and all_stops[current_idx + 1] - all_stops[last_idx] <= tank:
            current_idx += 1

        if current_idx == last_idx:
            # Cannot even reach the very next stop
            return -1

        if current_idx <= n:
            num_refills += 1

    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
