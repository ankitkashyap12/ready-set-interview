import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Merge Overlapping Intervals
 *
 * Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
 * and return an array of the non-overlapping intervals that cover all the intervals in the input.
 *
 * Sample Input:
 * intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
 *
 * Sample Output:
 * [[1, 2], [3, 8], [9, 10]]
 *
 * Time Complexity: O(n log n) due to sorting.
 * Space Complexity: O(n) to store the merged intervals.
 */
public class MergeOverlappingIntervals {
    public int[][] mergeOverlappingIntervals(int[][] intervals) {
        if (intervals == null || intervals.length <= 1) {
            return intervals;
        }

        // Sort based on start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> mergedInterval = new ArrayList<>();
        int[] currentInterval = intervals[0];
        mergedInterval.add(currentInterval);

        for (int[] nextInterval : intervals) {
            int currentIntervalEnd = currentInterval[1];
            int nextIntervalStart = nextInterval[0];
            int nextIntervalEnd = nextInterval[1];

            if (currentIntervalEnd >= nextIntervalStart) {
                currentInterval[1] = Math.max(currentIntervalEnd, nextIntervalEnd);
            } else {
                currentInterval = nextInterval;
                mergedInterval.add(currentInterval);
            }
        }
        return mergedInterval.toArray(new int[mergedInterval.size()][]);
    }
}

