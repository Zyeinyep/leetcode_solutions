class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach: Create a one-way mapping from s → t and ensure no two chars in s map to the same char in t.
        # Time: O(n)
        # Space: O(1) 

        if len(s) != len(t):
            return False

        mapping = {}
        taken = []
        for i in range(len(s)):
            curr_s = s[i]
            curr_t = t[i]
            if curr_s not in mapping:
                if curr_t in taken:
                    return False
                mapping[curr_s] = curr_t
                taken.append(curr_t)
            else:
                if mapping[curr_s] != curr_t:
                    return False 
               
        return True
