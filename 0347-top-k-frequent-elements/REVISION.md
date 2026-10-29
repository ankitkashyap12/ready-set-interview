# Top K Frequent Elements

- **Problem Number**: #022
- **Difficulty**: Medium
- **Topic**: Sorting & Heap
- **Pattern**: Bucket Sort / Min-Heap by Frequency
- **LeetCode Equivalent**: [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Active recall
How do you find the k most frequent elements in an array in strictly better than O(N log N) time?

## Core idea
Count frequencies using a hash map. Then use Bucket Sort where index represents frequency (0 to N). List<Integer>[] buckets = new List[n + 1]. Place each number into buckets[freq]. Iterate buckets from index N down to 0, collecting elements until k elements are gathered.

## Hints
- **Hint 1**: Frequencies are bounded between 1 and N. Does this allow linear-time bucket sorting?
- **Hint 2**: Array of lists where index = frequency avoids comparison-based sorting.

## Pattern
**Pattern**: Bucket Sort / Min-Heap by Frequency
Use when: Sorting & Heap problems require efficient traversal or optimal sub-structure.

## Trick
Bucket sort index corresponds to frequency. Since max frequency is N, iterating from bucket N down to 1 gives O(N) time.

## Complexity
Time: O(N) to count frequencies, populate buckets, and collect top k. Space: O(N) for map and buckets.

## Edge cases
- k equals number of unique elements.
- All elements have frequency 1.
- Negative numbers as values.
