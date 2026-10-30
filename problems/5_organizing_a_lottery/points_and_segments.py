# Uses python3
import sys

import bisect

def fast_count_segments(starts, ends, points):
    """
    Counts segments covering each point using binary search.
    A segment [s, e] covers point p iff s <= p and e >= p.
    Number of covering segments = count(starts <= p) - count(ends < p).
    Time Complexity: O((n + m) log n)
    Space Complexity: O(n)
    """
    sorted_starts = sorted(starts)
    sorted_ends = sorted(ends)
    cnt = []
    for p in points:
        starts_le = bisect.bisect_right(sorted_starts, p)
        ends_lt = bisect.bisect_left(sorted_ends, p)
        cnt.append(starts_le - ends_lt)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
