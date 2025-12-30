
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #Logic: Bakctracking
        #Space and time comp: O(n*4^n)
        res = []
        my_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, comb):
            if index == len(digits):
                res.append("".join(comb))
                return
            for i in my_dict[digits[index]]:
                comb.append(i)
                backtrack(index+1, comb)
                comb.pop()
        backtrack(0,[])
        return res
        
