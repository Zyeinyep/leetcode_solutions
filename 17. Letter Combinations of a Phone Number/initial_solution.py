
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
        for j in choices:
            print(j,type(j))

        def backtrack(comb, choices):
            if len(comb) == len(choices):
                res.append(comb)
                return
            for i in comb:
                for j in i:
                    comb.append(i)
                    backtrack(comb,choices)
                    comb.pop()
        backtrack([], choices)
        return res
        
