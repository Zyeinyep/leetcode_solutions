class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        choices = []
        my_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        for i in digits:
            choices.append(my_dict[int(i)])

        def backtrack(index, comb, choices):
            
            if len(comb) == len(choices):
                print(comb)

                res.append("".join(comb))
                return
            
            for i in choices[index]:
                comb.append(i)
                
                backtrack(index+1, comb,choices)
                comb.pop()
        backtrack(0,[], choices)
     
        return res
        
