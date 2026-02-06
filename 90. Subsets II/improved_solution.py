class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        nums.sort()
        def backtrack(curr, index):
    
            subsets.append(curr[:])
            for i in range(index,len(nums)):    
                if i > index and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
              
                backtrack(curr,i+1)
                curr.pop()

        backtrack([],0)
        return subsets
    
        
