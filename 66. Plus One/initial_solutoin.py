class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Runtime and Space complexity: O(n)
        carrier = 1
        digits = list(reversed(digits))
        
        for i,e in enumerate(digits):
            add = e + carrier
            if add > 9:
                carrier = 1
                s =  str(add)
                digits[i] = int(s[-1])

            else:
                carrier = 0
                digits[i] = add
        if carrier == 1:
            digits.append(1)
        digits = list(reversed(digits))

    
        return digits
        
