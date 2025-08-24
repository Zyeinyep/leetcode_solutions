"""
My approach:
1. Convert the list into a set to get all unique numbers.
2. For each unique number:
   - If it occurs more than twice in nums, find the first two positions.
   - Then iterate forward and remove extra occurrences using nums.pop().
   - Stop early once we see a larger number (since nums is sorted).
This works correctly, but it's inefficient because:
- nums.count() and nums.index() are O(n) each.
- nums.pop() in the middle is also O(n).
Overall, the solution can take O(n^2) time in the worst case.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        many = set(nums)
        
       
        for e in many:
            if nums.count(e) > 2:
                i = nums.index(e) + 2
                while i < len(nums):
                    if nums[i] == e:  
                        nums.pop(i)
                        continue
                    elif nums[i] >e:
                        break
                    i+=1
       
              
