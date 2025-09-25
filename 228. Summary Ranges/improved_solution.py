class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
      # Given a sorted list of unique integers, this function groups consecutive 
      # numbers into ranges. Single numbers are added as "x", while consecutive 
      # sequences are added as "x->y".

        res = []
        if not nums:
            return res
        
        start = nums[0]  # start of current range
        
        for i in range(1, len(nums) + 1):
            # if at end OR break in sequence
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    res.append(str(start))             # single number
                else:
                    res.append(str(start) + "->" + str(nums[i-1]))  # range
                if i < len(nums):  
                    start = nums[i]  # reset for next range
                    
        return res
