import java.util.Arrays;
import java.util.Scanner;

public class PointsAndSegments {

    /**
     * Counts segments covering each point using dual binary search.
     * Segments covering point p: count(starts <= p) - count(ends < p).
     * Time Complexity: O((n + m) log n)
     * Space Complexity: O(n)
     */
    private static int[] fastCountSegments(int[] starts, int[] ends, int[] points) {
        int[] sortedStarts = starts.clone();
        int[] sortedEnds = ends.clone();
        Arrays.sort(sortedStarts);
        Arrays.sort(sortedEnds);

        int[] cnt = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            int p = points[i];
            int countStartsLe = countLessOrEqual(sortedStarts, p);
            int countEndsLt = countLessThan(sortedEnds, p);
            cnt[i] = countStartsLe - countEndsLt;
        }
        return cnt;
    }

    private static int countLessOrEqual(int[] arr, int x) {
        int low = 0, high = arr.length;
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (arr[mid] <= x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    private static int countLessThan(int[] arr, int x) {
        int low = 0, high = arr.length;
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (arr[mid] < x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    private static int[] naiveCountSegments(int[] starts, int[] ends, int[] points) {
        int[] cnt = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < starts.length; j++) {
                if (starts[j] <= points[i] && points[i] <= ends[j]) {
                    cnt[i]++;
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, m;
        n = scanner.nextInt();
        m = scanner.nextInt();
        int[] starts = new int[n];
        int[] ends = new int[n];
        int[] points = new int[m];
        for (int i = 0; i < n; i++) {
            starts[i] = scanner.nextInt();
            ends[i] = scanner.nextInt();
        }
        for (int i = 0; i < m; i++) {
            points[i] = scanner.nextInt();
        }
        int[] cnt = fastCountSegments(starts, ends, points);
        for (int x : cnt) {
            System.out.print(x + " ");
        }
    }
}

