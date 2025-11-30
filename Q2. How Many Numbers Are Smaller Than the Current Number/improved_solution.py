class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        

        first_index = {}
        for i, val in enumerate(sorted_nums):
            if val not in first_index:
                first_index[val] = i
        

        return [first_index[n] for n in nums]
