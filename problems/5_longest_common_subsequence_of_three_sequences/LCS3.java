import java.util.*;

public class LCS3 {

    /**
     * Computes length of longest common subsequence of three sequences using 3D DP.
     * Time Complexity: O(|a| * |b| * |c|)
     * Space Complexity: O(|a| * |b| * |c|)
     */
    private static int lcs3(int[] a, int[] b, int[] c) {
        int p = a.length;
        int q = b.length;
        int r = c.length;
        int[][][] dp = new int[p + 1][q + 1][r + 1];

        for (int i = 1; i <= p; i++) {
            for (int j = 1; j <= q; j++) {
                for (int k = 1; k <= r; k++) {
                    if (a[i - 1] == b[j - 1] && b[j - 1] == c[k - 1]) {
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
                    } else {
                        dp[i][j][k] = Math.max(
                            dp[i - 1][j][k],
                            Math.max(dp[i][j - 1][k], dp[i][j][k - 1])
                        );
                    }
                }
            }
        }

        return dp[p][q][r];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int an = scanner.nextInt();
        int[] a = new int[an];
        for (int i = 0; i < an; i++) {
            a[i] = scanner.nextInt();
        }
        int bn = scanner.nextInt();
        int[] b = new int[bn];
        for (int i = 0; i < bn; i++) {
            b[i] = scanner.nextInt();
        }
        int cn = scanner.nextInt();
        int[] c = new int[cn];
        for (int i = 0; i < cn; i++) {
            c[i] = scanner.nextInt();
        }
        System.out.println(lcs3(a, b, c));
    }
}

