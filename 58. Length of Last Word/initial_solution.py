class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string into an array by spaces
        arr = s.split(" ")
        
       
        # Remove trailing empty strings from the end
        while arr[-1] == "":
            arr.pop()
        
        # Return the length of the last word
        return len(arr[-1])
