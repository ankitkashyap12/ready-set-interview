class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        One-pass Hash Map Complement Lookup.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
