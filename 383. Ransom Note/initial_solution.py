# This solution checks if ransomNote can be built from magazine 
# by simulating the removal of letters. It converts magazine into a list 
# (so characters can be popped out). Then for each character in ransomNote, 
# it looks for it in the magazine list:
#   - If found, it removes (pops) the first occurrence and increases count.
#   - If not found, construction fails (since no matching letter left).
# Finally, if the count of matched letters equals the ransomNote length, 
# it returns True; otherwise, False.

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
       
        count = 0
        s = list(magazine)

        for i in ransomNote:
            if i in s:
                count += 1
                s.pop(s.index(i))
          
        if count >= len(ransomNote):
            return True

        return False
