class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''Space and Time comp: O(n)'''
        memo={}
        def dp(i,j):
            if i<0 or j<0:
                return 0
            
                
            if (i,j) in memo:
                return memo[(i,j)]  
            if text1[i] == text2[j]:
                    res = 1 + dp(i-1, j-1)
            else:
                res = max(dp(i-1,j), dp(i,j-1))
            
            memo[(i,j)] = res
            return res
        longest = dp(len(text1)-1, len(text2)-1)
        return longest
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        
