import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
      


        """
        :type grid: List[List[int]]
        :rtype: int
        """

        visited = set()

        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))

        dirs = {(0,1), (0,-1), (1,0), (-1,0)}

        while heap:

            t, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            # once we reach the target, this is the minimum time
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return t

            for nx, ny in dirs:

                new_x = nx + x
                new_y = ny + y

                if (
                    0 <= new_x < len(grid)
                    and 0 <= new_y < len(grid[0])
                    and (new_x, new_y) not in visited
                ):

                    new_t = max(grid[new_x][new_y], t)

                    heapq.heappush(
                        heap,
                        (new_t, new_x, new_y)
                    )