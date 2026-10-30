import java.util.*;

public class CoveringSegments {

    /**
     * Finds the minimum set of points covering all segments.
     * Greedy strategy: sort by segment end points ascending.
     * Time Complexity: O(n log n)
     * Space Complexity: O(n)
     */
    private static int[] optimalPoints(Segment[] segments) {
        if (segments == null || segments.length == 0) {
            return new int[0];
        }

        Arrays.sort(segments, Comparator.comparingInt(s -> s.end));
        List<Integer> points = new ArrayList<>();
        int currentPoint = segments[0].end;
        points.add(currentPoint);

        for (int i = 1; i < segments.length; i++) {
            if (segments[i].start > currentPoint) {
                currentPoint = segments[i].end;
                points.add(currentPoint);
            }
        }

        int[] result = new int[points.size()];
        for (int i = 0; i < points.size(); i++) {
            result[i] = points.get(i);
        }
        return result;
    }

    private static class Segment {
        int start, end;

        Segment(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Segment[] segments = new Segment[n];
        for (int i = 0; i < n; i++) {
            int start, end;
            start = scanner.nextInt();
            end = scanner.nextInt();
            segments[i] = new Segment(start, end);
        }
        int[] points = optimalPoints(segments);
        System.out.println(points.length);
        for (int point : points) {
            System.out.print(point + " ");
        }
    }
}
 
