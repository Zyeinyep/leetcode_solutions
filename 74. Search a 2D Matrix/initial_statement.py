class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Approach: 
        First move up/down between rows to find a candidate row,
        then run a custom binary search on that row.
        
        Time: O(m + n^2) due to row-walking + array slicing in binary search  
        Space: O(n) because slicing creates new lists in each binary search
        """
       
        curr_row_index = len(matrix) // 2
        n = len(matrix)
       
        while 0 <= curr_row_index < n:

            curr_row = matrix[curr_row_index]
            value = curr_row[-1]
        
            if value > target:
                
                if curr_row_index == 0:
                    return self.binary_search(curr_row, target)

                prev_row = matrix[curr_row_index - 1]
                prev_val = prev_row[-1]

                if prev_val > target:
                    curr_row_index -= 1
                elif prev_val < target:
                    return self.binary_search(curr_row, target)
                else:
                    return True

            elif value < target:
                curr_row_index += 1
            else:
                return True

        return False

    def binary_search(self, arr, target):
        m = len(arr) // 2
        while len(arr) > 0:
            curr_value = arr[m]

            if curr_value > target:
                arr = arr[:m]
                m = len(arr) // 2

            elif curr_value < target:
                arr = arr[m+1:]
                m = len(arr) // 2

            else:
                return True

        return False
