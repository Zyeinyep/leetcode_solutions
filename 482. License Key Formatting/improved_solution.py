class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Time and Space complexity: O(n)
        s = s.replace("-", "").upper()
        res = []
        count = 0
        
        # Iterate from the end of the string
        for char in reversed(s):
            res.append(char)
            count += 1
            if count == k:
                res.append("-")  # add dash after k chars
                count = 0
        
        if res and res[-1] == "-":
            res.pop()  # remove trailing dash if any
        
        return "".join(reversed(res))
