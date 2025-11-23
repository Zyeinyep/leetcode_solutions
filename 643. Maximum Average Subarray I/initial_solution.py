# Finds max average of any subarray of length k using a sliding window.
# Time: O(n), Space: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -100000000
        s = 0
        max_ind = len(nums) - k + 1

        for i in range(max_ind):
            i2 = i + k
            if i == 0:
                s = sum(nums[i:i2])
            else:
                s = s - nums[i-1] + nums[i2-1]
            
            max_avg = max(max_avg, s / k)
                  
        return max_avg
