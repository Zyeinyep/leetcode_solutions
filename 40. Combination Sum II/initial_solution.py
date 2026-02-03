class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        comb = []
        def backtrack(curr, index, total):
            if total == target:
                comb.append(curr[:])
              
                return
            for i in range(index, len(candidates)):
                
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                e = candidates[i] 
                if total + e > target or e > target:
                    break
                curr.append(e)
        
                backtrack(curr, i + 1, total + e)
                curr.pop()
                
        backtrack([], 0, 0)
        return comb
