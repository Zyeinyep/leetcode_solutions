class Solution:
    def longestPalindrome(self, s: str) -> str:
      '''Technique used: 2 pointers moving outwards aka away from each other'''
        def pal_check(l,r):
            while 0<=l and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        result = ""
        for i,e in enumerate(s):
            odd = pal_check(i,i)
            even = pal_check(i,i+1)
            result = max(result, odd, even, key=len)
            print(odd,even,result)
        
        return result
    

            
