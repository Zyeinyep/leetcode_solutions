# Determines if a number is happy using Floyd's cycle detection.
# Logic:
# - Compute sum of squares of digits repeatedly.
# - Use two pointers (slow, fast) to detect a cycle.
# - If the number reaches 1, it's happy; if slow meets fast, a cycle exists.
# Time: O(log n * k), Space: O(1)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_number(num):
            return sum(int(d)**2 for d in str(num))

        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1
