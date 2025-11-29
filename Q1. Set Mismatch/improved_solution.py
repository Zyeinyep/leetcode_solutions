class Solution(object):
    def findErrorNums(self, nums):
        """
        Logic:
        - Sum of 1..n gives expected total.
        - Using sum(nums) and sum(set(nums)), we detect:
            • The duplicate number (appears twice)
            • The missing number (never appears)
        """

        n = len(nums)
        expected_sum = (n * (n + 1)) // 2

        # Sum without duplicate
        unique_sum = sum(set(nums))
        actual_sum = sum(nums)

        # Missing = expected_sum - unique_sum
        missed_number = expected_sum - unique_sum

        # Repeated = actual_sum - unique_sum
        repeated_number = actual_sum - unique_sum

        return [repeated_number, missed_number]
