class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        nums.sort()
        def backtrack(curr, index):
            if curr in subsets:
                return
            subsets.append(curr[:])
            for i in range(index,len(nums)):    
                curr.append(nums[i])
                print(index,i,nums[i],curr)
                backtrack(curr,i+1)
                curr.pop()

        backtrack([],0)
        return subsets
    
        
