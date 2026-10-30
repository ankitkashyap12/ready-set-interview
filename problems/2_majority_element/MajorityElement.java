import java.util.*;
import java.io.*;

public class MajorityElement {
    /**
     * Boyer-Moore Voting algorithm to find majority element in a[left...right-1].
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    private static int getMajorityElement(int[] a, int left, int right) {
        if (left >= right) {
            return -1;
        }
        int candidate = a[left];
        int count = 0;
        for (int i = left; i < right; i++) {
            if (count == 0) {
                candidate = a[i];
                count = 1;
            } else if (a[i] == candidate) {
                count++;
            } else {
                count--;
            }
        }

        // Verification pass
        int actualCount = 0;
        for (int i = left; i < right; i++) {
            if (a[i] == candidate) {
                actualCount++;
            }
        }
        return actualCount > (right - left) / 2 ? candidate : -1;
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        if (getMajorityElement(a, 0, a.length) != -1) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}

