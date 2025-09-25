# Approach:
# - Use collections.Counter to count the frequency of each character
#   in both strings.
# - If the two Counters are equal, then the strings are anagrams.

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters1 = Counter(s)   # count characters in first string
        letters2 = Counter(t)   # count characters in second string
      
        if letters1 == letters2:  # compare frequency counts
            return True
        
        return False
