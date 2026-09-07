from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        if x == 0 and y == 0:
            return 0

        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        q = deque()
        q.append((0, 0, 0))

        visited = {(0, 0)}

        while q:
            cX, cY, step = q.popleft()

            for dx, dy in directions:
                newX = cX + dx
                newY = cY + dy

                if newX == x and newY == y:
                    return step + 1

                if newX >= -2 and newY >= -2 and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    q.append((newX, newY, step + 1))
