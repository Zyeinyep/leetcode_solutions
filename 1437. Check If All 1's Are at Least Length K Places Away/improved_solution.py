# Check if all 1's in nums are at least k places apart
# Time: O(n), Space: O(1)
def kLengthApart(nums, k):
    prev = -10**10   
    
    for i, e in enumerate(nums):
        if e == 1:
            if i - prev - 1 < k:
                return False
            prev = i
    
    return True
