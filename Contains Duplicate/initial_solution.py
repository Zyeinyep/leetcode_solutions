from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for e in nums:
            if e in freq:
                return True
            freq.add(e)
        return False
