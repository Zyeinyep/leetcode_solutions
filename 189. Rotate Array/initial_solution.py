
from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        last = len(nums) - k
        arr = nums[:last]
        arr2 = nums[last:]
      
        p = arr2+arr

        for i,e in enumerate(nums):
            
            nums[i] = p[i]
            
        


            
                
                    
        
                    
            
        
