from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        f = defaultdict(list)
       
        for index, row in enumerate(board):
            for i2, element in enumerate(row):
                if element.isdigit():
                  
                    if self.check(f[element], index, i2):
                        return False
                    f[element].append((index,i2))

     
        return True
    def check(self, loc, row, column):
        
        for r,c in loc:
            if r == row:
                return True
            if c == column:
                return True
            if r//3 ==row//3 and c//3 == column//3:
                return True




        return False
                    
                    
        
