import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        dirs = {(0,1), (1,0), (-1,0), (0,-1)}


        q = []

        heapq.heappush(q, (0,0,0))
        visited = set()
        res = 0 
        while q:

            effort , x, y = heapq.heappop(q)
            
            if (x, y) in visited:
                continue
            visited.add((x,y))

            if x == len(heights)-1 and y == len(heights[0])-1:
                return effort


            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy

                if (0 <= new_x < len(heights) and
                    0 <= new_y < len(heights[0]) and
                    (new_x, new_y) not in visited):
                    diff = max(
                        effort,
                        abs(heights[new_x][new_y] - heights[x][y])
                    )
                    heapq.heappush(q, (diff, new_x, new_y))

        






        