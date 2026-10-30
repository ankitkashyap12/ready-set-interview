import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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
     * Approach 3: Two Pointers with Index Tracking
     * Time Complexity: O(n log n) - sorting array of paired (value, originalIndex).
     * Space Complexity: O(n) - for pair storage.
     */
    static int[] twoPointers(int[] nums, int target) {
        int[][] pairs = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            pairs[i][0] = nums[i];
            pairs[i][1] = i;
        }
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));

        int left = 0, right = nums.length - 1;
        while (left < right) {
            int sum = pairs[left][0] + pairs[right][0];
            if (sum == target) {
                return new int[]{pairs[left][1], pairs[right][1]};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return null;
    }

    /**
     * Approach 4: Hash Set (When returning values rather than indices)
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    static int[] twoSumValues(int[] nums, int target) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            int complement = target - num;
            if (set.contains(complement)) {
                return new int[]{complement, num};
            }
            set.add(num);
        }
        return null;
    }

    /**
     * Approach 5: Brute Force
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
