from collections import defaultdict

class Solution(object):
    def findErrorNums(self, nums):
        """

        Logic:
        - Count occurrences of each number using defaultdict.
        - The number with count==2 is the duplicate.
        - The number in range [1..n] not present in nums is the missing one.
        - Time and space complexity O(n)
        """

        n = defaultdict(int)
        k = []

        for x in nums:
            n[x] += 1
            if n[x] == 2:
                k.append(x)

    
        for i in range(1, len(nums) + 1):
            if i not in n:     
                k.append(i)

        return k
