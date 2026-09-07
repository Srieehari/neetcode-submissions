class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for i in range(9)]

        column = [set() for i in range(9)]

        boxes = [[set() for i in range(3)] for i in range(3)]
    

        for r in range(9):

            for c in range(9):


                val = board[r][c]

                if val == ".":

                    continue

                if val in row[r]:

                    return False
                if val in column[c]:

                    return False

                if val in boxes[r//3][c//3]:

                    return False


                row[r].add(val)
                column[c].add(val)

                boxes[r//3][c//3].add(val)

        return True




                



