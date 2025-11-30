class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s= []
        for i,e in enumerate(nums):
            arr = nums[:i] +nums[i+1:]
            count = 0
            for j,e1 in enumerate(arr):
                if e1<e:
                    count +=1
            s.append(count)
        return s
                    

        
