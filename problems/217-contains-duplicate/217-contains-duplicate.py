class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for x in nums:
            if x in found:
                return True
            else:
                found[x] = True
        return False