class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        graph = {}

        for from_i, to_i in tickets:

            if not from_i in graph:
                graph[from_i] = []

            heapq.heappush(graph[from_i], to_i)

        

        self.visited = set()

        self.res = []


        def dfs(flight):


            while flight in graph and graph[flight]:

                next_flight = heapq.heappop(graph[flight])
                dfs(next_flight)

            
            self.res.append(flight)
        dfs("JFK")

        return self.res[::-1]


        