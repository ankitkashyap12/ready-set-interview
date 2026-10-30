#Uses python3
import sys
import math

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    min_d = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_d = min(min_d, dist(points[i], points[j]))
    return min_d

def closest_split_pair(strip, d):
    min_d = d
    strip.sort(key=lambda p: p[1])
    n = len(strip)
    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            if strip[j][1] - strip[i][1] >= min_d:
                break
            min_d = min(min_d, dist(strip[i], strip[j]))
    return min_d

def closest_pair_rec(points_sorted_x):
    n = len(points_sorted_x)
    if n <= 3:
        return brute_force(points_sorted_x)

    mid = n // 2
    mid_x = points_sorted_x[mid][0]

    d_left = closest_pair_rec(points_sorted_x[:mid])
    d_right = closest_pair_rec(points_sorted_x[mid:])
    d = min(d_left, d_right)

    strip = [p for p in points_sorted_x if abs(p[0] - mid_x) < d]
    d_strip = closest_split_pair(strip, d)

    return min(d, d_strip)

def minimum_distance(x, y):
    """
    Finds the minimum Euclidean distance between a pair of points using Divide and Conquer.
    Time Complexity: O(n log^2 n) or O(n log n)
    Space Complexity: O(n)
    """
    points = sorted(zip(x, y), key=lambda p: p[0])
    return closest_pair_rec(points)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
