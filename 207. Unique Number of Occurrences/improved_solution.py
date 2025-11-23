# Optimized version using a set for counts
# Time: O(n), Space: O(n)

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = Counter(arr)
        counts = set()
        for val in occ.values():
            if val in counts:
                return False
            counts.add(val)
        return True
