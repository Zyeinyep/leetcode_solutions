class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Approach:
        # 1. Pick the last string in the list as the reference string.
        # 2. Compare each character of the reference string with the corresponding
        #    character in all the other strings.
        # 3. If a mismatch is found, or if a string is too short to continue,
        #    stop immediately.
        # 4. Accumulate matching characters into 'prefix' until a mismatch occurs.
        # 5. Return the longest common prefix that was built.

        ref = strs[-1]
        strs.pop()
        prefix = ""
        n = False

        for i, e in enumerate(ref):
            for el in strs:
                if i < len(el):
                    if el[i] != e:
                        n = True
                        break
                else:
                    n = True
                    break
            if n:
                break
            prefix += e
    
        return prefix
