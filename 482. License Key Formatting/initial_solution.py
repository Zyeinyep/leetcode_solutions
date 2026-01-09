class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        
        res =[]
        s = s.replace("-","").upper()

        first = len(s)%k
        if first:
            res.append(s[:first])
        
        for i in range(first, len(s),k):
            res.append(s[i:i+k])
        return "-".join(res)
