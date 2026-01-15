class Solution:
    # Time complexity: O( n^(target/minValue) × k × log(k) )
    # Space complexity: O((target/minValue) + output_size + k)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []

        def backtrack(nums):
            if sum(nums) == target:
                nums = sorted(nums)
                if sorted(nums) not in combs:
                    combs.append(sorted(nums))
                    
            
            for i in candidates:
                if sum(nums) + i > target:
                    continue
                nums.append(i)
                backtrack(nums)
                nums.pop()

        backtrack([])
      
        return combs
        
