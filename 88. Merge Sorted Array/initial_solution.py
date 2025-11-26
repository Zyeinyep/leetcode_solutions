class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Logic: merge first m elements of nums1 with nums2, sort, write back.
        Time: O((m+n) log (m+n))
        Space: O(m+n)
        """
        arr = nums1[:m] + nums2  
        arr.sort()            
        for i, e in enumerate(arr):
            nums1[i] = e         
