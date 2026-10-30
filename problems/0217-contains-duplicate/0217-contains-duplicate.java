import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Approach 1: Hash Set Early-Exit (Optimal)
     * Time Complexity: O(n) average
     * Space Complexity: O(n)
     */
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numset = new HashSet<>(nums.length);
        for (int num : nums) {
            if (!numset.add(num)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Approach 2: Sorting (Constant Auxiliary Space)
     * Time Complexity: O(n log n)
     * Space Complexity: O(1) or O(log n) depending on sort implementation
     */
    public boolean containsDuplicateSorting(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 1; i < sorted.length; i++) {
            if (sorted[i] == sorted[i - 1]) {
                return true;
            }
        }
        return false;
    }
}
