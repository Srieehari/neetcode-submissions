class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset= []

        candidates.sort()
        def dfs(index, curr_sum):




            if curr_sum > target:

                return 

            elif curr_sum == target:

                

                res.append(subset.copy())
                return

            if index >= len(candidates):

                return 

            

            subset.append(candidates[index])

            curr_sum += candidates[index]

            

            dfs(index+1, curr_sum)

            subset.pop()
            curr_sum -= candidates[index]

            next_index = index + 1

            while next_index < len(candidates) and candidates[next_index] == candidates[index]:

                next_index +=1

            

            dfs(next_index, curr_sum)

        dfs(0,0)

        return res