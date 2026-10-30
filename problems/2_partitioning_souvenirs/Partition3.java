import java.util.*;
import java.io.*;

public class Partition3 {
    /**
     * 3-Way Equal Partition using 2D DP table.
     * dp[s1][s2] = true if subset sums s1 and s2 can be formed simultaneously.
     * Time Complexity: O(n * (sum/3)^2)
     * Space Complexity: O((sum/3)^2)
     */
    private static int partition3(int[] A) {
        int total = 0;
        for (int x : A) total += x;
        if (total % 3 != 0 || A.length < 3) return 0;
        int target = total / 3;

        boolean[][] dp = new boolean[target + 1][target + 1];
        dp[0][0] = true;

        for (int num : A) {
            for (int s1 = target; s1 >= 0; s1--) {
                for (int s2 = target; s2 >= 0; s2--) {
                    if (dp[s1][s2]) {
                        if (s1 + num <= target) dp[s1 + num][s2] = true;
                        if (s2 + num <= target) dp[s1][s2 + num] = true;
                    }
                }
            }
        }
        return dp[target][target] ? 1 : 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = scanner.nextInt();
        }
        System.out.println(partition3(A));
    }
}

