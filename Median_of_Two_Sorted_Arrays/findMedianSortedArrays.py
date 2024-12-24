
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       
        mylist = nums1+nums2
        s = sorted(mylist)
        length = len(s)
        
        median = 0
        if length % 2 ==0:
            m = length / 2
            median = float(s[m] + s[m-1])/2
            

        else:
            m = round(length / 2,1)
            median = s[int(m)]
        return median
       

   
        
