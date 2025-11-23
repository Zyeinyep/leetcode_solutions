class Solution(object):
    def minimumOperations(self, nums):
        """
        Counts how many numbers are not divisible by 3.

        Logic: +1 for every e where e % 3 != 0.
        Time: O(n)
        Space: O(1)
        """
        count = 0

        for e in nums:
            if e % 3 != 0:
                count += 1

        return count
