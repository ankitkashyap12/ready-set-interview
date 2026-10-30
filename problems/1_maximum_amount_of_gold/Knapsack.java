import java.util.*;

public class Knapsack {
    /**
     * 0-1 Knapsack without repetition to find maximum weight of gold that fits in capacity W.
     * Time Complexity: O(n * W)
     * Space Complexity: O(W) using backwards rolling 1D array
     */
    static int optimalWeight(int W, int[] w) {
        int[] dp = new int[W + 1];
        for (int weight : w) {
            for (int j = W; j >= weight; j--) {
                dp[j] = Math.max(dp[j], dp[j - weight] + weight);
            }
        }
        return dp[W];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int W, n;
        W = scanner.nextInt();
        n = scanner.nextInt();
        int[] w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = scanner.nextInt();
        }
        System.out.println(optimalWeight(W, w));
    }
}

