import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Three Number Sum (Triple Sum)
 *
 * Write a function that takes in a non-empty array of distinct integers and an
 * integer representing a target sum. The function should find all triplets in
 * the array that sum up to the target sum and return a two-dimensional array of
 * all these triplets.
 *
 * Time Complexity: O(n^2) - sorting takes O(n log n), nested two-pointer scan takes O(n^2).
 * Space Complexity: O(n) for the output list of triplets.
 */
public class TripleSum {

    public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
        Arrays.sort(array);
        List<Integer[]> tripletsList = new ArrayList<>();

        for (int i = 0; i < array.length - 2; i++) {
            int left = i + 1;
            int right = array.length - 1;

            while (left < right) {
                int cSum = array[i] + array[left] + array[right];
                if (cSum == targetSum) {
                    tripletsList.add(new Integer[]{array[i], array[left], array[right]});
                    left++;
                    right--;
                } else if (cSum < targetSum) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return tripletsList;
    }
}
