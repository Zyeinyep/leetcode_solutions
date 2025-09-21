class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Approach:
        - If the list is empty, return "" immediately.
        - Use the first string as a reference.
        - For each character in the reference string (left to right):
            * Compare it with the character at the same position in all other strings.
            * If a mismatch is found, or if one string ends, return the prefix up to that point.
        - If no mismatches are found, the whole first string is the common prefix.
        
        Time Complexity: O(N * M) 
            - N = number of strings
            - M = length of the shortest string
        Space Complexity: O(1)
        """
        if not strs:
            return ""
        
        # Use the first string as reference
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]
