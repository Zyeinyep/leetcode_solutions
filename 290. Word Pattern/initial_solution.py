class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.strip().split()
        map = {}
        seen = []
        if len(s) != len(pattern):
            return False
        for i,e in enumerate(pattern):
            if e in map:
                if map[e] != s[i]:
                    return False
            else:
                if s[i] in seen:
                    return False
                map[e] = s[i]
                seen.append(s[i])

        return True
       
            
