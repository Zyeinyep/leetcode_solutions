 """
        Time:  O(n*m) — try each position in haystack and compare up to m chars.
        Space: O(1) — only a few variables; no extra growing data structures.

        Logic: Slide over haystack; at each index check if the substring of length
               needle matches. Return the first index where it matches, else -1.
        """
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
      
        i2 = len(haystack) - len(needle) + 1
        for i in range(i2):
            arr = haystack[i:i+len(needle)]
            if arr == needle:
                return i
        return -1
        
