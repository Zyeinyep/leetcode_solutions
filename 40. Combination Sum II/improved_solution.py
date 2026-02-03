class Solution:
    def combinationSum2(self, candidates, target):
       # Pass remaining target instead of maintaining total.
       # Keep your duplicate-skip and sorted-early-break — those are optimal tricks.
        candidates.sort()
        res, path = [], []

        def dfs(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
               
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                val = candidates[i]
                if val > remain: 
                    break
                path.append(val)
                dfs(i + 1, remain - val)
                path.pop()

        dfs(0, target)
        return res
