# Checks if a number is happy by repeatedly summing the squares of its digits.
# Stops if it reaches 1 (happy) or falls into a cycle.
# Time: O(log n * k), Space: O(1)
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        m = n
    
        while True:
            print("i",n)
            l = 0
            for i in n:
                i = int(i)
                l += i*i
            n = str(l)
            print(n)
            if int(n)<4 or n == m:
                break
        
        if int(n) == 1:
            return True
        return False



                
        
