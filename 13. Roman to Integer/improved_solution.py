class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer to Roman numeral using greedy subtraction.

        Logic:
        - Use a descending list of Roman values (including subtractive forms).
        - Repeatedly append the largest symbol ≤ num and subtract its value.
        
        Time: O(1)   (num ≤ 3999 so at most ~15 steps)
        Space: O(1)
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"), (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),  (4, "IV"),
            (1, "I")
        ]
        
        roman = []
        
        for value, symbol in vals:
            while num >= value:
                roman.append(symbol)
                num -= value
        
        return "".join(roman)
