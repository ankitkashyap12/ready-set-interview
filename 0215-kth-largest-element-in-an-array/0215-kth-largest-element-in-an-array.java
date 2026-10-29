import java.util.PriorityQueue;
import java.util.Random;

class Solution {
    /**
     * Approach 1: Min-Heap of Size k
     * Keep a min-heap of size k. After iterating through all elements,
     * the root of the heap contains the kth largest element.
     * Time Complexity: O(n log k)
     * Space Complexity: O(k)
     */
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> (a - b));
        for (int num : nums) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.poll();
    }

    /**
     * Approach 2: Quickselect (Hoare's Selection Algorithm)
     * Target index in 0-indexed sorted order: targetIndex = nums.length - k.
     * Partitions the array around a random pivot.
     * Time Complexity: O(n) average, O(n^2) worst-case.
     * Space Complexity: O(1) auxiliary space (iterative).
     */
    public int findKthLargestQuickSelect(int[] nums, int k) {
        int targetIndex = nums.length - k;
        int left = 0;
        int right = nums.length - 1;
        Random random = new Random();

        while (left <= right) {
            int pivotIndex = left + random.nextInt(right - left + 1);
            int partitionIndex = partition(nums, left, right, pivotIndex);
            if (partitionIndex == targetIndex) {
                return nums[partitionIndex];
            } else if (partitionIndex < targetIndex) {
                left = partitionIndex + 1;
            } else {
                right = partitionIndex - 1;
            }
        }
        return nums[left];
    }

    private int partition(int[] nums, int left, int right, int pivotIndex) {
        int pivotValue = nums[pivotIndex];
        swap(nums, pivotIndex, right); // move pivot to end
        int storeIndex = left;

        for (int i = left; i < right; i++) {
            if (nums[i] < pivotValue) {
                swap(nums, storeIndex, i);
                storeIndex++;
            }
        }
        swap(nums, storeIndex, right); // move pivot to final position
        return storeIndex;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}