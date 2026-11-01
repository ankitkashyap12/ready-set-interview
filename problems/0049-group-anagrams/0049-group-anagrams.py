from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams using character count tuple as dictionary key.
        Time Complexity: O(N * K) where N = len(strs), K = max(len(s))
        Space Complexity: O(N * K)
        """
        grouped = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            grouped[tuple(count)].append(s)
        return list(grouped.values())

    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams using sorted string as key.
        Time Complexity: O(N * K log K)
        Space Complexity: O(N * K)
        """
        grouped = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            grouped[key].append(s)
        return list(grouped.values())
