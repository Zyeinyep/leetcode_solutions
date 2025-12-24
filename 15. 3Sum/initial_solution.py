class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for i,e in enumerate(nums):
            target = -e
            my_dict = {}
            for j in range(i+1, len(nums)):
                need = target-nums[j]
                if need in my_dict:
                    res.add(tuple(sorted((e,need,nums[j]))))
                else:
                    my_dict[nums[j]] = 1
        return [list(t) for t in res]

            


            
        
