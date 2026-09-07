class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        


        mapping = {a:[] for a in range(numCourses)}



        for a,b in prerequisites:

            mapping[a].append(b)


        
        visited = set()

        def dfs(num):

            if mapping[num] == []:

                return True

            if num in visited:

                return False

            

            visited.add(num)
            for val in mapping[num]:

                if not dfs(val):

                    return False

            visited.remove(num)
            mapping[num] = []

            return True

        for i in range(numCourses):

            if not dfs(i):
                return False

        return True

            

            