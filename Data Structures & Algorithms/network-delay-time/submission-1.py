class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:



        graph = {}
        for i in range(1,n+1):
            graph[i] =[]



        for u,v,t in times:

            graph[u].append((v,t))


        q = []

        heapq.heappush(q,(0,k))
        visited = set()

        while q:

            time, node = heapq.heappop(q)

            if node in visited:
                continue

            visited.add((node))
            if len(visited) == n:
                return time

            for p, t in graph[node]:

                if p in visited:
                    continue

                heapq.heappush(q, (time + t, p))

        return -1

        



        