# Finds the maximum average of any subarray of length k.
# Logic:
# - Compute the sum of the first k elements.
# - Slide the window by one element at a time:
#     subtract the element leaving, add the element entering.
# - Track the maximum sum and divide by k at the end for average.
# Time: O(n) — each element is visited once.
# Space: O(1) — only a few variables are used.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
