import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # time and space complexity" O(nlogn)
        fact = math.factorial(n)
        fact = str(fact)
        i = len(fact) - 1
        count = 0

        while True:
            if int(fact[i]) == 0:
                count += 1
            else:
                return count
            i = i - 1

        
