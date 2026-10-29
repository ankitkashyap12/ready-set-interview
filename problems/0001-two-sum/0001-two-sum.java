import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Optimized one-pass hash map: O(n) time, O(n) space
        return optimized(nums, target);
    }

    /**
     * Approach 1: One-Pass Hash Table (Optimal)
     * Time Complexity: O(n) - single pass through the array.
     * Space Complexity: O(n) - hash table stores at most n elements.
     */
    static int[] optimized(int[] nums, int target) {
        Map<Integer, Integer> indexAndNums = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int targetNum = target - nums[i];
            if (indexAndNums.containsKey(targetNum)) {
                return new int[]{indexAndNums.get(targetNum), i};
            }
            indexAndNums.put(nums[i], i);
        }
        return null;
    }

    /**
     * Approach 2: Two-Pass Hash Table
     * Time Complexity: O(n) - two separate passes.
     * Space Complexity: O(n)
     */
    static int[] twoPassHashTable(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{i, map.get(complement)};
            }
        }
        return null;
    }

    /**
     * Approach 3: Brute Force
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    static int[] brute(int[] nums, int sum) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == sum) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }
}
