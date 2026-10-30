/**
 * Array of Products (Product of Array Except Self)
 *
 * Write a function that takes in a non-empty array of integers and returns an
 * array of the same length, where each element in the output array is equal to
 * the product of every other number in the input array.
 * Solve this without using division.
 */
public class ArrayOfProducts {

    /**
     * Approach 1: Brute Force
     * Time Complexity: O(n^2)
     * Space Complexity: O(n) for output array
     */
    public int[] arrayOfProductsBrute(int[] array) {
        int[] products = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            int product = 1;
            for (int j = 0; j < array.length; j++) {
                if (i != j) {
                    product *= array[j];
                }
            }
            products[i] = product;
        }
        return products;
    }

    /**
     * Approach 2: Left and Right Product Arrays
     * Time Complexity: O(n)
     * Space Complexity: O(n) auxiliary space
     */
    public int[] arrayOfProductsOptimal(int[] array) {
        int[] leftProducts = new int[array.length];
        int[] rightProducts = new int[array.length];
        int leftProd = 1;
        int rightProd = 1;
        int[] products = new int[array.length];

        for (int i = 0; i < array.length; i++) {
            leftProducts[i] = leftProd;
            leftProd *= array[i];
        }

        for (int i = array.length - 1; i >= 0; i--) {
            rightProducts[i] = rightProd;
            rightProd *= array[i];
        }

        for (int i = 0; i < array.length; i++) {
            products[i] = leftProducts[i] * rightProducts[i];
        }
        return products;
    }

    /**
     * Approach 3: In-Place Single Result Array (Optimal)
     * Builds prefix products directly in output array, then folds suffix product from right.
     * Time Complexity: O(n)
     * Auxiliary Space: O(1) (excluding output array)
     */
    public int[] arrayOfProductsOptimal2(int[] array) {
        int[] products = new int[array.length];
        int leftProd = 1;
        int rightProd = 1;

        for (int i = 0; i < array.length; i++) {
            products[i] = leftProd;
            leftProd *= array[i];
        }

        for (int i = array.length - 1; i >= 0; i--) {
            products[i] *= rightProd;
            rightProd *= array[i];
        }

        return products;
    }
}

