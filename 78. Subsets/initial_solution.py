class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time complexity: O(n · 2ⁿ)
        # Space complexity: O(n · 2ⁿ)
        sub = []
        def backtrack(curr, start):
            if len(curr) <= len(nums):
                sub.append(curr[:])
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(curr,i+1)
                curr.pop()

        backtrack([],0)
        return sub
        
