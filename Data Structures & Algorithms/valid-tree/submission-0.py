class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        mapping={i:[] for i in range(n)}

        for a,b in edges:

            mapping[a].append(b)
            mapping[b].append(a)
        

        visited = set()

        def dfs(num, prev):


            if num in visited:

                return False

            visited.add(num)

            for i in mapping[num]:

                if prev == i:

                    continue

                if dfs(i, num) == False:

                    return False     
            return True


        return dfs(0, -1) and len(visited) == n




        


        