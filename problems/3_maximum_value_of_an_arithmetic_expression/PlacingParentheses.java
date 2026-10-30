import java.util.Scanner;

public class PlacingParentheses {
    /**
     * Finds maximum value of an arithmetic expression using interval DP.
     * Time Complexity: O(n^3) where n is the number of operands.
     * Space Complexity: O(n^2)
     */
    private static long getMaximValue(String exp) {
        int n = (exp.length() + 1) / 2;
        long[] digits = new long[n];
        char[] ops = new char[n - 1];

        for (int i = 0; i < exp.length(); i++) {
            if (i % 2 == 0) {
                digits[i / 2] = exp.charAt(i) - '0';
            } else {
                ops[i / 2] = exp.charAt(i);
            }
        }

        long[][] m = new long[n][n];
        long[][] M = new long[n][n];

        for (int i = 0; i < n; i++) {
            m[i][i] = digits[i];
            M[i][i] = digits[i];
        }

        for (int s = 1; s < n; s++) {
            for (int i = 0; i < n - s; i++) {
                int j = i + s;
                long minVal = Long.MAX_VALUE;
                long maxVal = Long.MIN_VALUE;

                for (int k = i; k < j; k++) {
                    long a = eval(M[i][k], M[k + 1][j], ops[k]);
                    long b = eval(M[i][k], m[k + 1][j], ops[k]);
                    long c = eval(m[i][k], M[k + 1][j], ops[k]);
                    long d = eval(m[i][k], m[k + 1][j], ops[k]);

                    minVal = Math.min(minVal, Math.min(Math.min(a, b), Math.min(c, d)));
                    maxVal = Math.max(maxVal, Math.max(Math.max(a, b), Math.max(c, d)));
                }

                m[i][j] = minVal;
                M[i][j] = maxVal;
            }
        }

        return M[0][n - 1];
    }

    private static long eval(long a, long b, char op) {
        if (op == '+') {
            return a + b;
        } else if (op == '-') {
            return a - b;
        } else if (op == '*') {
            return a * b;
        } else {
            assert false;
            return 0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String exp = scanner.next();
        System.out.println(getMaximValue(exp));
    }
}

