# Finds the final value of 'original' after repeatedly doubling it
# if it exists in the array 'nums'.
# Logic:
# - While 'original' exists in nums, double it.
# - Stop when 'original' is not in nums and return it.
# Time: O(n * log(max_value)), worst case each doubling checks the entire list.
# Space: O(1), only a few variables used.

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        count = 0
        while True:
            if count == 0 and original not in nums:
                return original
            else:
                if original in nums:
                    count += 1
                    original = original * 2
                else:
                    return original
