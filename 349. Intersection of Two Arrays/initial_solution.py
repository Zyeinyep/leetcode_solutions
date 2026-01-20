class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set()
        for i in nums1:
            if i in nums2:
                inter.add(i)
        return list(inter)
