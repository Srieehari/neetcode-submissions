from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        coords = set()
        islands = 0

        def bfs(row, column):
            q = deque()
            q.append((row, column))
            coords.add((row, column))

            while q:
                r0, c0 = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    nr, nc = r0 + dr, c0 + dc
                    if (0 <= nr < r and 0 <= nc < c and
                        grid[nr][nc] == "1" and (nr, nc) not in coords):
                        coords.add((nr, nc))
                        q.append((nr, nc))

        for row in range(r):
            for column in range(c):
                if grid[row][column] == "1" and (row, column) not in coords:
                    islands += 1
                    bfs(row, column)

        return islands
