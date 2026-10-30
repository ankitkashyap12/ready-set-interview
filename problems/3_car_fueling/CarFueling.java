import java.util.*;
import java.io.*;

public class CarFueling {
    /**
     * Greedy car fueling: refill at the furthest reachable gas station.
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    static int computeMinRefills(int dist, int tank, int[] stops) {
        int n = stops.length;
        int[] allStops = new int[n + 2];
        allStops[0] = 0;
        System.arraycopy(stops, 0, allStops, 1, n);
        allStops[n + 1] = dist;

        int numRefills = 0;
        int currentIdx = 0;

        while (currentIdx <= n) {
            int lastIdx = currentIdx;
            while (currentIdx <= n && allStops[currentIdx + 1] - allStops[lastIdx] <= tank) {
                currentIdx++;
            }
            if (currentIdx == lastIdx) {
                return -1; // cannot reach next station
            }
            if (currentIdx <= n) {
                numRefills++;
            }
        }
        return numRefills;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dist = scanner.nextInt();
        int tank = scanner.nextInt();
        int n = scanner.nextInt();
        int stops[] = new int[n];
        for (int i = 0; i < n; i++) {
            stops[i] = scanner.nextInt();
        }

        System.out.println(computeMinRefills(dist, tank, stops));
    }
}
