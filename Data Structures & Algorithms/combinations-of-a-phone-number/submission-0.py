class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) <= 0:

            return []


        dig = {

            "2": "abc",
            "3": "def",
            "4":"ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9":"wxyz"
        }

        res = []
        


        def dfs(string, i):

            if i >= len(digits):
                res.append(string)

                return






            for let in dig[digits[i]]:

                

                dfs(string + let, i+1)

        dfs("", 0)

        return res

                






