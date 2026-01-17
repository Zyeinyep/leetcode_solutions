class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Runtime: O(C(n, k) · k)
        # Space comp: O(C(n, k) · k)
        comb = []
        def backtrack(curr,start):
            if len(curr) == k:
                comb.append(curr[:])
            for i in range(start, n - (k - len(curr)) + 2):
                curr.append(i)
                backtrack(curr,i+1)
                curr.pop()
        backtrack([],1)
        return comb
