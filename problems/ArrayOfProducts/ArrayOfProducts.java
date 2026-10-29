package arrays;

/**
 * @author Ankit Kashyap on 10-09-2023
 * <p>
 * Write a function that takes in a non-empty array of integers and returns an
 * array of the same length, where each element in the output array is equal to
 * the product of every other number in the input array.
 * </p>
 * <p>
 * In other words, the value at <span>output[i]</span> is equal to the product of
 * every number in the input array other than <span>input[i]</span>.
 * </p>
 * <p>Note that you're expected to solve this problem without using division.</p>
 */
public class ArrayOfProducts {

    public int[] arrayOfProductsBrute(int[] array) {
        // BruteForce
        //O(n^2)
        int[] products = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            int product = 1;
            for (int j = 0; j < array.length; j++) {
                if (i != j) {
                    product *= array[j];
                }
                products[i] = product;
            }
        }
        return products;
    }

    public int[] arrayOfProductsOptimal(int[] array) {
        // we can store the product we have already calculated
        //we will store all product left of that indices and right of indices in 2 array.
        // product of respective left*right indices in those array will be product
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

    public int[] arrayOfProductsOptimal2(int[] array) {
        // we can store the product we have already calculated
        //we will store all product left of that indices and right of indices in 2 array.
        // product of rspective left*right indices in those array will be product
        // same as sol2 but one step combined
        int[] leftProducts = new int[array.length];
        int[] rightProducts = new int[array.length];
        int leftProd = 1;
        int rightProd = 1;
        int[] products = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            products[i] = leftProd; //start storing left prod in final araay itself
            leftProd *= array[i];
        }


        for (int i = array.length - 1; i >= 0; i--) {
            products[i] *= rightProd; //then multiply it with right one. no need for third loop
            rightProd *= array[i];
        }

        return products;
    }
}
