class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        if target in nums:
            return nums.index(target)
        for i,e in enumerate(nums):
            if e>target:
                return i
            elif target<e and i == 0:
                return 0
            elif target> e and i == len(nums) -1:
                return len(nums)
        
        
