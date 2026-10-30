import java.util.Arrays;
import java.util.Scanner;

public class FractionalKnapsack {
    static class Item implements Comparable<Item> {
        double value;
        double weight;
        double unitValue;

        Item(double value, double weight) {
            this.value = value;
            this.weight = weight;
            this.unitValue = weight > 0 ? value / weight : 0;
        }

        @Override
        public int compareTo(Item other) {
            return Double.compare(other.unitValue, this.unitValue); // descending
        }
    }

    /**
     * Fractional Knapsack greedy algorithm.
     * Time Complexity: O(n log n)
     * Space Complexity: O(n)
     */
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double totalValue = 0;
        int n = values.length;
        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            items[i] = new Item(values[i], weights[i]);
        }
        Arrays.sort(items);

        double remainingCapacity = capacity;
        for (Item item : items) {
            if (remainingCapacity <= 0) break;
            double take = Math.min(remainingCapacity, item.weight);
            totalValue += take * item.unitValue;
            remainingCapacity -= take;
        }

        return totalValue;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        System.out.println(getOptimalValue(capacity, values, weights));
    }
} 
