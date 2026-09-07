
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        row = len(grid)
        column = len(grid[0])

        minutes = 0
        q = deque()

        fresh = 0 


        for r in range(row):

            for c in range(column):

                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:

                    fresh +=1

                
        self.rotten = 0
        def search(r,c):
            if not r in range(row) or not c in range(column) or grid[r][c] != 1:

                return
            
            grid[r][c] = 2
            self.rotten +=1
            q.append((r,c))

        while q:

            for i in range(len(q)):

                r, c = q.popleft()
                search(r+1, c)
                search(r-1, c)
                search(r, c+1)
                search(r, c-1)
            if q:
                minutes +=1

        
        if self.rotten != fresh:

            return -1

        else:
            return minutes

                
                    



                    