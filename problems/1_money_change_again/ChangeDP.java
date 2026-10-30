import java.util.Scanner;

public class ChangeDP {
    /**
     * Compute minimum coins to change money m using coins 1, 3, 4 with Dynamic Programming.
     * Recurrence: dp[i] = min(dp[i - c] + 1) for c in {1, 3, 4}
     * Time Complexity: O(m)
     * Space Complexity: O(m)
     */
    private static int getChange(int m) {
        if (m <= 0) return 0;
        int[] dp = new int[m + 1];
        int[] coins = {1, 3, 4};
        for (int i = 1; i <= m; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int coin : coins) {
                if (i >= coin && dp[i - coin] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[m];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));

    }
}

