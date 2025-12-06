class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Approach:
        Treat the 2D matrix as a sorted 1D array and perform normal binary search.

        Time:  O(log(m * n))
        Space: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
