class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = 0
        a = list(reversed(a))
        b = list(reversed(b))
        sol = []
        
      
        while i < max(len(a), len(b)) or carry:
            curr_a = 0
            curr_b = 0
            if i < len(a):
                curr_a = int(a[i])
            if i < len(b):
                curr_b = int(b[i])
            
            total = curr_a + curr_b + carry 
            
            if total == 2:
                carry = 1
                sol.append('0')
            elif total == 3:
                carry = 1
                sol.append('1')
            else:
                carry = 0
                sol.append(str(total))
            
            i += 1
        
        return ''.join(sol[::-1])
