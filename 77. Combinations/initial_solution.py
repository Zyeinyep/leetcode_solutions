class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
      # Space: O(C(n, k) * k)
      # Time: O(C(n, k) * k)
        comb = []
        def backtrack(curr,start):
            if len(curr) == k:
                comb.append(curr[:])
            for i in range(start,n+1):
                curr.append(i)
                backtrack(curr,i+1)
                curr.pop()
        backtrack([],1)
        return comb
