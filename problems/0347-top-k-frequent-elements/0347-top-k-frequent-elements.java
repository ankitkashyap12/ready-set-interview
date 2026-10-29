import java.util.*;

class Solution {
    /**
     * Approach 1: Frequency Map + Min-Heap
     * Count frequencies, then maintain a min-heap of size k.
     * Time Complexity: O(n log k)
     * Space Complexity: O(n + k)
     */
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numFreq = new HashMap<>();
        for (int num : nums) {
            numFreq.put(num, numFreq.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> (numFreq.get(a) - numFreq.get(b)));
        for (int num : numFreq.keySet()) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        int[] result = new int[k];
        int i = 0;
        while (!pq.isEmpty()) {
            result[i] = pq.poll();
            i++;
        }
        return result;
    }

    /**
     * Approach 2: Bucket Sort (Optimal O(n) Time)
     * Since frequency cannot exceed nums.length, map frequency to an array of lists (buckets).
     * Then collect elements from the highest frequency buckets down to 1 until k elements are found.
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    @SuppressWarnings("unchecked")
    public int[] topKFrequentBucketSort(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // buckets[i] contains all numbers that appear with frequency i
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int num : countMap.keySet()) {
            int freq = countMap.get(num);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        int[] result = new int[k];
        int idx = 0;
        for (int freq = buckets.length - 1; freq >= 1 && idx < k; freq--) {
            if (buckets[freq] != null) {
                for (int num : buckets[freq]) {
                    result[idx++] = num;
                    if (idx == k) {
                        break;
                    }
                }
            }
        }
        return result;
    }
}


