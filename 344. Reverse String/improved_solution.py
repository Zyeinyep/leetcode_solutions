class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]


        
