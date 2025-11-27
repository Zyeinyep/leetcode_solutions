# Logic:
# Process the number digit-by-digit from highest place value. For each place, determine the Roman
# numeral contribution, handling subtractive cases (4 and 9) separately, and append the correct symbol.
# Continue reducing the number until all place values are converted.

# Time Complexity: O(n), where n is the number of digits (max 4 → effectively O(1)).
# Space Complexity: O(1), using only constant-size maps and strings.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        fives = {1:'V',2:'L', 3:'D'}
        ones = {1:'I',2:'X',3:'C',4:'M'}
        while num > 0:
            num = str(num)
            curr_num = num[0]+(len(num)-1)*'0'
            
            if curr_num[0] == '4' or curr_num[0] == '9':
                if curr_num[0] == '4':
                    r = ones[len(curr_num)] + fives[len(curr_num)]
                    roman += r
                else:
                    r = ones[len(curr_num)] + ones[len(curr_num)+1]
                    roman += r
                num = int(num) - int(curr_num)
            else:
                if int(curr_num) % 1000 == 0:
                    roman += ones[4]
                    num = int(num) - 1000
                    continue
                if int(curr_num) < int(str(5) + '0' * (len(curr_num) - 1)):
                    roman += ones[len(curr_num)]
                    num = int(num) - int(str(1) + '0' * (len(curr_num) - 1))
                else:
                    roman += fives[len(curr_num)]  
                    num = int(num) - int(str(5) + '0' * (len(curr_num) - 1))
        
        return roman
