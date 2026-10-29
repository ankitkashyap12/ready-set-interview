class Solution {
    /**
     * Approach 1: Two Pointers (Optimal)
     * Since array is sorted in non-decreasing order:
     * - If sum < target, increment left pointer to increase sum.
     * - If sum > target, decrement right pointer to decrease sum.
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[]{left + 1, right + 1};
            }
            if (sum > target) {
                right--;
            } else {
                left++;
            }
        }
        return null;
    }

    /**
     * Approach 2: Binary Search (Alternative)
     * For each index i, binary search for (target - numbers[i]) in index range [i + 1, n - 1].
     * Time Complexity: O(n log n)
     * Space Complexity: O(1)
     */
    public int[] twoSumBinarySearch(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            int complement = target - numbers[i];
            int low = i + 1;
            int high = numbers.length - 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (numbers[mid] == complement) {
                    return new int[]{i + 1, mid + 1};
                }
                if (numbers[mid] < complement) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return null;
    }
}