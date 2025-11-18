# The function collects the indices of all 1s, then compares consecutive positions to ensure the gap is > k.
# If any pair of 1s is too close, it returns False; otherwise, it returns True.
# Time Complexity: O(n), where n = len(nums), because we iterate through the array twice
# Space Complexity: O(m), where m = number of 1s, because we store their indices in a list


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dict = []
        for i, e in enumerate(nums):
            if e == 1:
                dict.append(i)
        
        for i, e in enumerate(dict):
            if i + 1 < len(dict):
                if e + k >= dict[i+1]:
                    return False
        return True
