class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Logic: Count consecutive 1s. Reset to 0 when hitting a 0.
        Track the maximum streak.

        Time:  O(n)  – single pass
        Space: O(1)  – constant variables
        """

        max_cons = 0
        curr = 0

        for e in nums:
            if e == 1:
                curr += 1
            else:
                curr = 0
            max_cons = max(max_cons, curr)

        return max_cons
