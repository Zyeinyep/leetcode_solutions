# Approach:
# - Iterate through nums and group consecutive numbers into sublists (curr).
# - If numbers are consecutive, keep extending the current group.
# - If not, save the group into ranges and start a new one.
# - After building ranges, format them into strings:
#     - Single number becomes "x"
#     - A range becomes "x->y"
# - Return the final list of string ranges.

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []   # stores groups of consecutive numbers
        curr = []     # stores the current consecutive range we are building
        
        for i, e in enumerate(nums):
            if i == 0:
                curr.append(e)
               
            if i + 1 < len(nums):   # check next element
                if curr[-1] + 1 == nums[i+1]:   # consecutive
                    curr.append(nums[i+1])
                else:   # break in sequence → close current group
                    ranges.append(curr)
                    curr = [nums[i+1]]
            else:
                ranges.append(curr)  # last element goes into ranges
               
        final_r = []
        for i in ranges:
            if len(i) == 1:   # single number
                final_r.append(str(i[0]))
            else:             # range from min to max
                mi = i[0]
                ma = i[-1]
                final_r.append(str(mi) + "->" + str(ma))

        print(final_r)
        return final_r
