class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows, columns = len(heights), len(heights[0])


        pac, atl = set(), set()


        def dfs(r,c, vist, prev):


            if not r in range(rows) or not c in range(columns) or heights[r][c] < prev or (r,c) in vist:
                return

            vist.add((r,c))

            dfs(r+1,c, vist, heights[r][c])
            dfs(r-1,c, vist, heights[r][c])
            dfs(r,c+1, vist, heights[r][c])
            dfs(r,c-1, vist, heights[r][c])
            


        for c in range(columns):

            dfs(0, c, pac, 0)
            dfs(rows-1, c, atl, 0)

        for r in range(rows):

            dfs(r, 0, pac, 0)
            dfs(r, columns-1, atl,0)

        res = []

        for r in range(rows):
            for c in range(columns):

                if (r,c) in atl and (r,c) in pac:

                    res.append((r,c))

        return res

                



