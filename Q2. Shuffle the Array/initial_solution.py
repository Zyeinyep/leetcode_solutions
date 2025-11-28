class Solution(object):
    def shuffle(self, nums, n):
        """
        Given nums = [x1, x2, ... xn, y1, y2, ... yn],
        return the shuffled form [x1, y1, x2, y2, ...].

        Time Complexity:  O(n)
            - We loop through half of the array and append elements twice.
        
        Space Complexity: O(n)
            - We create two halves of size n/2 and a final array of size n.
        """

        length = len(nums) // 2  # Number of pairs (n)

        # First half contains x1...xn
        arr = nums[:length]

        # Second half contains y1...yn
        arr1 = nums[length:]

        final_arr = []

        # Interleave the pairs: xi, yi
        for i in range(length):
            final_arr.append(arr[i])   # Add xi
            final_arr.append(arr1[i])  # Add yi

        return final_arr
