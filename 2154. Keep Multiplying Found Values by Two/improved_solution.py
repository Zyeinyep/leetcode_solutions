# Optimized version using a set for faster lookups
# Time: O(n + log(max_value)), Space: O(n)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original
