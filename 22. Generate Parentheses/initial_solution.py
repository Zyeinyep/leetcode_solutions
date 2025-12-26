class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Logic used: Backtracking
        # Time and Space complexity: O(n*Cn)
        result = []
        
        def backtrack(combination,num_open,num_close):
            if len(combination) == 2*n:
                result.append("".join(combination))
                return
            
            if num_open < n:
                combination.append("(")
                backtrack(combination, num_open + 1, num_close)
                combination.pop()

            if num_close < num_open:
                combination.append(")")
                backtrack(combination, num_open, num_close + 1)
                combination.pop()
            
        backtrack([],0,0)
        return result
        
        
