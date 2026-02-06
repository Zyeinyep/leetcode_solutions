class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        comb = []
        nums.sort()
        n = len(nums)
        v = [False]*n
        def backtrack(path, v):
            if len(path) == n:
                comb.append(path[:])
                return
            for i in range(0,n):
                if v[i]:
                    continue
                if i - 1 > -1:
                    if i > 0 and nums[i] == nums[i-1] and not v[i-1]:
                        continue
                    
                path.append(nums[i])
                v[i] = True
                backtrack(path,v)                    
                path.pop()
                v[i] = False
            
        backtrack([], v)
        return comb
