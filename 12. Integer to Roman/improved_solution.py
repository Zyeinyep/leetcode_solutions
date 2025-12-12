class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer to Roman numeral using a greedy approach.

        Logic:
        - Use a descending list of Roman numeral values (including subtractive forms:
          900, 400, 90, 40, 9, 4).
        - For each value, append its symbol while it fits into the remaining number.
        - Subtract that value and continue until num becomes 0.
        - This works because Roman numerals are constructed from highest → lowest symbols.

        Time Complexity: O(1)
            The input range is fixed (1–3999), so the loop runs a constant number
            of iterations regardless of input.

        Space Complexity: O(1)
            Aside from a small result list, no additional space grows with input.
        """

        val = [
            1000, 900, 500, 400,
            100,  90,  50,  40,
            10,   9,   5,   4,
            1
        ]

        # Corresponding symbols for each value above.
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        res = []

     
        for i in range(len(val)):
         
            while num >= val[i]:
                num -= val[i]
                res.append(syms[i])

        return "".join(res)
