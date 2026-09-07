class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        




        mapping = {i:[] for i in range(numCourses)}





        for a,b in prerequisites:


            mapping[a].append(b)

        
        visited = set()
        cycle = set()

        res = []


        def dfs(num):

            if num in cycle:
                return False

            if num in visited:
                return True

            cycle.add(num)
            for i in mapping[num]:

                if dfs(i) == False:
                    return False

            res.append(num)

            visited.add(num)

            cycle.remove(num)

        for num in range(numCourses):

            if dfs(num) == False:

                return []
        return res


        


            
        


            

           

            


        

                

            





            



            
