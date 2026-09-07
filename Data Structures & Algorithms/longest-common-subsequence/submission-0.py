class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = len(text1)
        cols = len(text2)


        arr = [[0]*(cols+1) for i in range(rows+1)]



        for r in range(rows-1, -1,-1):


            for c in range(cols-1,-1,-1):


                if text1[r] == text2[c]:

                    arr[r][c] = 1 + arr[r+1][c+1]

                else:

                    arr[r][c] = max(arr[r+1][c], arr[r][c+1])


        return arr[0][0]





         