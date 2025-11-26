class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Optimal: fill nums1 from the end using three pointers.
        Time: O(m+n)
        Space: O(1)
        """
        i = m - 1       # pointer for nums1
        j = n - 1       # pointer for nums2
        k = m + n - 1   # fill position in nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
