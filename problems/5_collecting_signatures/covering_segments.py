# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    """
    Finds the minimum number of points needed to cover all segments.
    Greedy strategy: sort segments by end coordinate ascending and pick end of segment.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not segments:
        return []
    # Sort by end point
    sorted_segments = sorted(segments, key=lambda s: s.end)
    points = []
    current_point = sorted_segments[0].end
    points.append(current_point)

    for s in sorted_segments[1:]:
        if s.start > current_point:
            current_point = s.end
            points.append(current_point)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
