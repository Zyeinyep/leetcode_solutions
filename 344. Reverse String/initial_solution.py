class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Time complexity: O(n)
        # Space complexity: O(1)
        l = len(s)
        if len(s) % 2 == 0:
            m = len(s)/2 - 1
        else:
            m = len(s)/2 
        for i in range(m + 1):
            temp = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = temp
            print(s[i],s[len(s)-1-i])

        
