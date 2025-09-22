class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Check rows and columns first
        if not self.check(board):
            return False
        
        # Build and check 3x3 boxes
        for i in (0, 3, 6):
            box1, box2, box3 = [], [], []
            for j in (0, 1, 2):
                box1.extend(board[i+j][0:3])
                box2.extend(board[i+j][3:6])
                box3.extend(board[i+j][6:9])
            
            if not self.check(box1):
                return False
            if not self.check(box2):
                return False
            if not self.check(box3):
                return False
             
        return True

    def check(self, board):
        # If board is a flat 1D list (box)
        if isinstance(board[0], str):
            for i, e1 in enumerate(board):
                if e1 != ".":
                    other_elements = board[:i] + board[i+1:]
                    if e1 in other_elements:
                        return False
            return True
        
        # Otherwise, board is 2D: check rows
        for row in board:
            for i, e1 in enumerate(row):
                if e1 != ".":
                    other_elements = row[:i] + row[i+1:]
                    if e1 in other_elements:
                        return False
                    
        # Check columns
        for i in range(len(board[0])):
            column = [row[i] for row in board]
            for j, e1 in enumerate(column):
                if e1 != ".":
                    other_elements = column[:j] + column[j+1:]
                    if e1 in other_elements:
                        return False
        return True
