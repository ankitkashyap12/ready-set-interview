import java.util.Scanner;

public class Change {
    /**
     * Minimum coins to change m with coin denominations 10, 5, 1.
     * Greedy choice property holds because denominations are canonical.
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    private static int getChange(int m) {
        int tens = m / 10;
        int rem = m % 10;
        int fives = rem / 5;
        int ones = rem % 5;
        return tens + fives + ones;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));

    }
}

