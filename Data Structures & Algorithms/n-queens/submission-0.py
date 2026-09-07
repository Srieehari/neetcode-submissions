class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        diag1 = set()

        diag2 = set()

        cols = set()


        res = []

        board = [["."]*n for i in range(n)]

        def dfs(r):

            if r == n:

                copy = ["".join(row) for row in board]

                res.append(copy)

                return 

            for c in range(n):


                if c in cols or (c+r) in diag1 or (r-c) in diag2:

                    continue
                board[r][c] = "Q"

                diag1.add(r+c)
                diag2.add(r-c)
                cols.add(c)

                dfs(r+1)

                board[r][c] = "."
                diag1.remove(r+c)
                diag2.remove(r-c)
                cols.remove(c)

        dfs(0)

        return res




            





        