class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Best solution: simple, readable, optimal.

        Time Complexity:  O(n)
            - We loop from 0 to n-1 and append two elements each iteration.
        
        Space Complexity: O(n)
            - We build a new result list of size 2n.
            - No extra arrays created besides the output.
        """

        res = []

        for i in range(n):
            res.append(nums[i])     # xi
            res.append(nums[i+n])   # yi

        return res
