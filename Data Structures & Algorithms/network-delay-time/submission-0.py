class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}

        for u, v, w in times:
            if u not in adj_list:
                adj_list[u] = []

            adj_list[u].append((w, v))

        heap = [(0, k)]

        visited = set()
        time = 0

        while heap:

            dist, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            time = dist

            for weight, neighbor in adj_list.get(node, []):

                heapq.heappush(
                    heap,
                    (dist + weight, neighbor)
                )

        if len(visited) != n:
            return -1

        return time
        