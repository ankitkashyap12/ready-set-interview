from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if array contains duplicates using hash set lookup.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
