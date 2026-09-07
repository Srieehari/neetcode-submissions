class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}

        for fr, to in tickets:
            if not fr in adj_list:
                adj_list[fr] = []
            heapq.heappush(adj_list[fr], to)

        res = []
        

        def dfs(node):
            
            heap = adj_list.get(node, [])
            while heap:

                dest = heapq.heappop(heap)

                dfs(dest)
            res.append(node)
            return

        dfs("JFK") 
        return res[::-1]

            

        
        
        