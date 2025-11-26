class Solution:
    # Logic: transpose matrix, then reverse each row (in-place rotation).
    # Time: O(n^2)
    # Space: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: reverse each row
        for i in range(n):
            matrix[i].reverse()
