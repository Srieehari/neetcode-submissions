class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges)+1)]

        rank = [1]*(len(edges)+1)

        res = []     



        def find(num):


            while num != par[num]:

                par[num] = par[par[num]]


                num = par[num]

            return num

        def union(n1, n2):


            val1 = find(n1)
            val2 = find(n2)


            if val1 == val2:


                return True

            

            if rank[val1] < rank[val2]:

                rank[val2] += rank[val1]

                par[val1] = val2
            else:

                rank[val1] += rank[val2]

                par[val2] = val1

            return False

        

        for a,b in edges:

            if union(a,b):

                return [a,b]

        return res[-1]





