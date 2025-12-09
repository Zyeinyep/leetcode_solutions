class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        w = 1
        if len(s):
            longest = 1
        else:
            longest = 0
        for i,e in enumerate(s):
            while True:
                if i+w > len(s):
                    break

                arr = s[i:i+w]
                if len(arr) == len(set(arr)):
                    longest = w
                    w += 1
                else:
                    break


        return longest
             

