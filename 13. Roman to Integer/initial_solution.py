class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert Roman numeral to integer using subtractive rule.

        Logic:
        - Scan left to right.
        - If a smaller value comes before a larger value, subtract it.
        - Otherwise, add it.

        Time: O(n)
        Space: O(1)
        """
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        total = 0
        for i in range(len(s)):
            # If current < next → subtract, else add
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
