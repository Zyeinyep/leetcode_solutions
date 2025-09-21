class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(" ")
        print(arr)
        while arr[-1] == "":
            arr.pop()
        return len(arr[-1])
        
