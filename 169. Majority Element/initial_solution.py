import math

# This solution finds the majority element in a list of integers.
# The majority element is defined as the element that appears more than ⌊n/2⌋ times.
# The code converts the list into a set (to avoid duplicate checks), then iterates
# through each unique element and counts its frequency in the original list.
# If an element’s count is greater than ⌊n/2⌋, it is returned as the majority element.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        n = len(nums)
        times = math.floor(n/2)
        
        for i, e in enumerate(set_nums):
            if nums.count(e) > times:
                return e
