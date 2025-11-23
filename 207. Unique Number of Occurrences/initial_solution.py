# Checks if the number of occurrences of each value in the array is unique.
# Logic:
# - Count occurrences of each element using Counter.
# - Store the counts in a list.
# - If a count repeats, return False.
# - Otherwise, return True.
# Time: O(n), where n is the length of the array.
# Space: O(n), for the Counter and the list of counts.

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = Counter(arr)  # count occurrences of each element
        lens = []
        for key, value in occ.items():
            if value in lens:  # check if this count already exists
                return False
            lens.append(value)
        return True
