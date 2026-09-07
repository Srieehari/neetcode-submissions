from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        column = len(grid[0])
        visited = set()
        q = deque()

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        steps = 0

        def func(r, c):
            if (
                r not in range(row) or
                c not in range(column) or
                (r, c) in visited or
                grid[r][c] != 2147483647
            ):
                return
            q.append((r, c))
            visited.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps
                func(r + 1, c)
                func(r - 1, c)
                func(r, c + 1)
                func(r, c - 1)
            steps += 1
