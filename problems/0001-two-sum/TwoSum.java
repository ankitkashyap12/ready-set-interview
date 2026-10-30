import java.util.*;

/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 *
 * Approaches:
 * 1. Hash Map (Indices lookup): O(n) time, O(n) space
 * 2. Two Pointers after Sorting: O(n log n) time, O(1) space
 * 3. Hash Set (Value lookup when indices not required): O(n) time, O(n) space
 */
public class TwoSum {

    // Approach 1: Hash Map (O(n) time, O(n) space)
    public static int[] twoNumberSumUsingMap(int[] array, int targetSum) {
        Map<Integer, Integer> indicesValue = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            int diff = targetSum - array[i];
            Integer diffInd = indicesValue.get(diff);
            if (diffInd != null) {
                return new int[]{array[diffInd], array[i]};
            }
            indicesValue.put(array[i], i);
        }
        return new int[0];
    }

    // Approach 2: Two Pointers with Sorting (O(n log n) time, O(1) space)
    public static int[] twoSumBinary(int[] array, int targetSum) {
        int[] sorted = array.clone();
        Arrays.sort(sorted);

        int left = 0;
        int right = sorted.length - 1;
        while (left < right) {
            int currentSum = sorted[left] + sorted[right];
            if (currentSum == targetSum) {
                return new int[]{sorted[left], sorted[right]};
            } else if (currentSum < targetSum) {
                left++;
            } else {
                right--;
            }
        }
        return new int[0];
    }

    // Approach 3: Hash Set (O(n) time, O(n) space)
    public static int[] twoSumUsingSet(int[] array, int target) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : array) {
            int targetNum = target - num;
            if (numSet.contains(targetNum)) {
                return new int[]{targetNum, num};
            }
            numSet.add(num);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int sum = 5;
        int[] arr = new int[]{1, 2, 3};
        int[] result = twoSumUsingSet(arr, sum);
        System.out.println(result[0] + " " + result[1]);
    }
}

