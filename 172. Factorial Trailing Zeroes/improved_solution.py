class Solution(object):
    def trailingZeroes(self, n):
        """
        Time Complexity: O(log₅ n)
        Space Complexity: O(1)

        Logic:
        A trailing zero is created by a factor of 10 → (2 × 5).
        Since there are always more 2s than 5s in factorials, the number of zeros
        depends only on how many times 5 is a factor in numbers from 1 to n.

        We repeatedly divide n by 5 to count:
        - How many numbers contribute at least one 5
        - How many contribute multiple 5s (like 25, 125, etc.)
        Each division adds the count of factors of 5.
        """
        count = 0
        while n > 0:
            n //= 5      # Count how many multiples of 5, 25, 125... are ≤ n
            count += n   # Add all those 5 factors to our total
        return count
