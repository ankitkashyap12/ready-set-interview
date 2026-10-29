package arrays;

import java.util.Arrays;

/**
 * @author Ankit Kashyap on 27-08-2023
 * <p>
 * <p>
 * Write a function that takes in a non-empty array of integers that are sorted
 * in ascending order and returns a new array of the same length with the squares
 * of the original integers also sorted in ascending order.
 */
public class SortedSquaredArray {

    private static int[] sortedSquaredBrute(int[] array) {
        //sorting again before returning
        //O(nlogn) time
        int[] squaredArray = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            int num = array[i];
            squaredArray[i] = num * num;
        }
        Arrays.sort(squaredArray);
        return (squaredArray);
    }

    private static int[] sortedSquaredBruteUsinLambda(int[] array) {
        return Arrays.stream(array).map(x -> x * x).sorted().toArray();

    }

    public static void main(String[] args) {
        int[] arr = new int[]{-10, 10, 5, 0};
        int[] squared = sortedSquaredBruteUsinLambda(arr);
        int[] squaredBrute = sortedSquaredBrute(arr);
        int[] squaredOptimal = sortedSquaredArrayOptimal(arr);
        System.out.println(squaredBrute.equals(squared));
        for (int num : squaredOptimal) {
            System.out.println(num);
        }
    }

    public static int[] sortedSquaredArrayOptimal(int[] array) {
        // since arrays may contain negative hence the squared value randomise the order
//        to overcome this we will start from both end and compare absolute value , we know whichever is is larger among these that square should be in output array in
//        reverse position as no other remaining element's square can be greater
        //O(n) and O(n) space
        int left = 0;
        int right = array.length - 1;
        int[] squared = new int[array.length];
        for (int i = array.length - 1; i >= 0; i--) {
            if (Math.abs(array[left]) > Math.abs(array[right])) {
                squared[i] = array[left] * array[left];
                left++;
            } else {
                squared[i] = array[right] * array[right];
                right--;
            }
        }
        return squared;
    }
}
