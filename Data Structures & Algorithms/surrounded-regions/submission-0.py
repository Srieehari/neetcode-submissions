class Solution:
    def solve(self, board: List[List[str]]) -> None:




        rows = len(board)
        columns = len(board[0])



        safe = set()


        def bfs(r,c):


            if not r in range(rows) or not c in range(columns) or board[r][c] != "O" or (r,c) in safe:
                return

            safe.add((r,c))

            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)





        for r in range(rows):

            for c in range(columns):


                if board[r][c] == "O" and (r == 0 or r == rows-1 or c== 0 or c== columns-1):


                    bfs(r,c)

        for r in range(rows):

            for c in range(columns):
                if board[r][c] == "O" and not (r,c) in safe:

                    board[r][c] = "X"


                
        