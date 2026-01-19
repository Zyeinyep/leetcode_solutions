class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        changed = []
        def backtrack(curr,index):
            if index == len(s):
                changed.append("".join(curr))
                return
            char = s[index]
            curr.append(char)
            backtrack(curr,index+1)
            curr.pop()
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                curr.append(char.swapcase())
                backtrack(curr,index+1)
                curr.pop()
             
        backtrack([],0)
        return changed
        
        
