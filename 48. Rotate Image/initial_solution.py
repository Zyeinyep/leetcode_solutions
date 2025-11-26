import copy

class Solution:
    # Logic: copy matrix, then place each element into its rotated position.
    # Time: O(n^2)
    # Space: O(n^2) (due to deep copy)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m_copy = copy.deepcopy(matrix)
        
        l = len(matrix[0])
        print(l)
        for i in range(l):
            for j in range(l):
                matrix[j][l-i-1] = m_copy[i][j]
               
        print(m_copy)
