import java.util.*;

class EditDistance {
  /**
   * Computes the minimum edit distance (Levenshtein distance) between strings s and t.
   * Operations allowed: insertion, deletion, substitution (each cost 1).
   *
   * Time Complexity: O(|s| * |t|)
   * Space Complexity: O(|s| * |t|) (can be reduced to O(min(|s|, |t|))
   */
  public static int EditDistance(String s, String t) {
    int m = s.length();
    int n = t.length();
    int[][] dp = new int[m + 1][n + 1];

    for (int i = 0; i <= m; i++) {
      dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
      dp[0][j] = j;
    }

    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        if (s.charAt(i - 1) == t.charAt(j - 1)) {
          dp[i][j] = dp[i - 1][j - 1];
        } else {
          dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
        }
      }
    }

    return dp[m][n];
  }
  public static void main(String args[]) {
    Scanner scan = new Scanner(System.in);

    String s = scan.next();
    String t = scan.next();

    System.out.println(EditDistance(s, t));
  }

}
