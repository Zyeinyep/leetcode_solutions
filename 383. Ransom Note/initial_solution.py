# Approach:
# Use collections.Counter to count how many times each character 
# appears in both ransomNote and magazine. 
# Subtracting two Counters (rn - mg) keeps only the positive differences 
# (letters still missing in the magazine). 
# If rn - mg is empty, then all characters needed are available, so return True.
# Otherwise, return False.

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rn = Counter(ransomNote)
        mg = Counter(magazine)
        
        return not (rn - mg)
