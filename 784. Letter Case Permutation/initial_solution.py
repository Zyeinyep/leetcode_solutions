class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Time and Space comp: O(n · 2^k)
        # n= len(s), k=number of letters
        changed = []
        def backtrack(curr,index):
            if index == len(s):
                changed.append("".join(curr[:]))
                return
            curr.append(s[index])
            backtrack(curr,index+1)
            curr.pop()
            if s[index].isalpha():
                curr.append(s[index].swapcase())
                backtrack(curr,index+1)
                curr.pop()
             
        backtrack([],0)
        return changed
        
        
