class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = m 
        cols = n

        ways = [[0]*(cols+1) for i in range(row+1)]

        ways[row][cols-1] = 1

        



        for r in range(row-1,-1,-1):

            for c in range(cols-1,-1,-1):


                ways[r][c] = ways[r+1][c] + ways[r][c+1]

        

        return ways[0][0]

        






        
        