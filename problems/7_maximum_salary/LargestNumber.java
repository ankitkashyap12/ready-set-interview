import java.util.*;

public class LargestNumber {
    /**
     * Composes the largest number from an array of numeric strings.
     * Greedy comparator: x precedes y if (x + y) > (y + x).
     * Time Complexity: O(n log n * L)
     * Space Complexity: O(n)
     */
    private static String largestNumber(String[] a) {
        Arrays.sort(a, (x, y) -> (y + x).compareTo(x + y));
        if (a.length > 0 && a[0].equals("0")) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : a) {
            sb.append(s);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] a = new String[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.next();
        }
        System.out.println(largestNumber(a));
    }
}

