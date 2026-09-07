class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        



        par = [i for i in range(n)]

        rank = [1]*n


        def find(num):


            while num != par[num]:

                par[num] = par[par[num]]


                num = par[num]

            return num

        def union(num1, num2):


            val1 = find(num1)
            val2 = find(num2)


            if val1 == val2:

                return 0 

            if rank[val2] > rank[val1]:


                par[val1] = val2

                rank[val2] += rank[val1]

            else:

                par[val2] = val1

                rank[val1] += rank[val2]
            return 1
        tot = n
        for a,b in edges:

            tot -= union(a,b)

        return tot



        
            

            