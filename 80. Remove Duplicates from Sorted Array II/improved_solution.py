"""
        :type nums: List[int]
        :rtype: int

        Approach (Two Pointers):
        - Since the array is sorted, duplicates are always grouped together.
        - We allow the first two elements automatically (k starts at 2).
        - For each new element (starting at index 2):
            * Compare it with nums[k-2].
            * If it's different, copy it to nums[k] and move k forward.
            * If it's the same, skip it (prevents more than 2 duplicates).
        - The array is modified in-place, and k is the new length.
        
        Time Complexity: O(n)  (single pass)
        Space Complexity: O(1) (in-place, no extra storage)
        """
class Solution(object):
    def removeDuplicates(self, nums):
    
        k = 2
        for i in range(2, len(nums)):
             print(nums[i],i,k-2)
             if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            
        return k
