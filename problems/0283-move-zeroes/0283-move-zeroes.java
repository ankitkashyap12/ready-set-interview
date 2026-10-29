class Solution {
    /**
     * Approach 1: Two Pointers (In-Place Swapping)
     * Maintains the invariant that all elements before `nonZero` are non-zeros in original order.
     * Skips self-swaps when i == nonZero to minimize memory write cycles.
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public void moveZeroes(int[] nums) {
        int nonZero = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                if (i != nonZero) {
                    int temp = nums[nonZero];
                    nums[nonZero] = nums[i];
                    nums[i] = temp;
                }
                nonZero++;
            }
        }
    }

    /**
     * Approach 2: Overwrite and Fill (Minimizes write operations when mostly zeros)
     * Shifts non-zero elements forward, then fills the remaining tail with zeros.
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public void moveZeroesFill(int[] nums) {
        int insertPos = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[insertPos++] = num;
            }
        }
        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }
}