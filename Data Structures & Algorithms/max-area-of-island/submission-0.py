from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        area = 0 
        islands = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            islands.add((r, c))
            total = 1

            while q:
                r0, c0 = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r0 + dr, c0 + dc
                    if (
                        0 <= nr < row and
                        0 <= nc < column and
                        (nr, nc) not in islands and
                        grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        islands.add((nr, nc))
                        total += 1
            return total

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 and (r, c) not in islands:
                    area = max(area, bfs(r, c))

        return area


