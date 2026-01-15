class Solution:
    # Several big changes have been made: we are not calculating sum of current array everytime
    # instead passing a var total, that keeps us from using sum() every time 
    # after adding an element to the array we are only considering elements including itself and afterwards  in teh next run
    # This will prevent duplications such as [2,3,2] and [2,2,3]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()

        def backtrack(start,nums,total):
            if total == target:
                combs.append(nums[:])
                    
            for i in range(start, len(candidates)):
                curr = candidates[i]
                if total + curr > target:
                    break
                nums.append(curr)
                backtrack(i,nums, total+ curr)
                nums.pop()

        backtrack(0,[],0)
      
        return combs
        
