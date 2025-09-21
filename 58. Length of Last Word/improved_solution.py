class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing spaces from the string
        # Example: "Hello World   " -> "Hello World"
        stripped = s.strip()

        # Split the string by whitespace into words
        # Example: "Hello World" -> ["Hello", "World"]
        words = stripped.split()

        # Take the last word from the list and return its length
        # Example: ["Hello", "World"] -> "World" -> length = 5
        return len(words[-1])
