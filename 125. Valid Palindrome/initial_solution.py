class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
     

        i = 0
        i2 = len(s) - 1
        while i < i2:
            if s[i].isalnum() and s[i2].isalnum():
                if s[i].lower() != s[i2].lower():
                    return False
                else:
                    i += 1
                    i2 -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[i2].isalnum():
                    i2 -= 1
        return True
