import java.util.*;

public class DifferentSummands {
    /**
     * Represents n as a sum of maximum number of pairwise distinct positive integers.
     * Time Complexity: O(sqrt(n))
     * Space Complexity: O(sqrt(n))
     */
    private static List<Integer> optimalSummands(int n) {
        List<Integer> summands = new ArrayList<>();
        int k = 1;
        while (n > 2 * k) {
            summands.add(k);
            n -= k;
            k++;
        }
        summands.add(n);
        return summands;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> summands = optimalSummands(n);
        System.out.println(summands.size());
        for (Integer summand : summands) {
            System.out.print(summand + " ");
        }
    }
}

