import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        """
        :type points: List[List[int]]
        :rtype: int
        """

        adj_list = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                if (x1, y1) not in adj_list:
                    adj_list[(x1, y1)] = []

                if (x2, y2) not in adj_list:
                    adj_list[(x2, y2)] = []

                adj_list[(x1, y1)].append((dist, x2, y2))
                adj_list[(x2, y2)].append((dist, x1, y1))

        start = tuple(points[0])

        heap = [(0, start[0], start[1])]
        visited = set()

        total = 0

        while heap and len(visited) < len(points):

            d, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            total += d

            for n_d, n_x, n_y in adj_list.get((x, y), []):

                if (n_x, n_y) in visited:
                    continue

                heapq.heappush(
                    heap,
                    (n_d, n_x, n_y)
                )

        return total