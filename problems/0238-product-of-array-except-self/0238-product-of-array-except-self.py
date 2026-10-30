from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates products of array except self in O(n) time and O(1) extra space.
        """
        n = len(nums)
        res = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
