class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        comb = []

        def backtrack(nums, path, total, elements):
            if total == n and elements == k:
                comb.append(path[:])
                return
            for i in range(nums,10):
                if elements > k or total > n:
                    return
                path.append(i)
                backtrack(i + 1, path, total + i, elements + 1)
                path.pop()


        backtrack(1,[],0, 0)
        return comb
        
