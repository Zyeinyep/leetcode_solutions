class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Logic: backtracking
        # Time and Space comp: O(n*n!)
        res = []
        def backtrack(perm, nums):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in nums:
                if i in perm:
                    continue
                perm.append(i)
                backtrack(perm,nums)
                perm.pop()
        backtrack([],nums)
        return res
        
        
