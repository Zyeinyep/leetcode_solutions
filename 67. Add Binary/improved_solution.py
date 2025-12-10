class Solution:
    def addBinary(self, a, b):
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        sol = []
        

        while i >= 0 or j >= 0 or carry:
            curr_a = int(a[i]) if i >= 0 else 0
            curr_b = int(b[j]) if j >= 0 else 0
            
            total = curr_a + curr_b + carry
            sol.append(str(total % 2)) 
            carry = total // 2          
            
            i -= 1
            j -= 1
        
    
        return ''.join(sol[::-1])
