class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                # Box index
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check duplicates
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                
                # Add to sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
                
        return True
