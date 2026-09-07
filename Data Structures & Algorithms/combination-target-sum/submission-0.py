class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        subset = []


        def helper(index, curr_sum ):


            if curr_sum > target:

                return 

            elif curr_sum == target:

                res.append(subset.copy())
                return

            if index>= len(nums):

                return 


            subset.append(nums[index])

            curr_sum += nums[index]

            helper(index, curr_sum)

            subset.pop()
            curr_sum-= nums[index]

            helper(index+1, curr_sum)

        helper(0, 0)


        return res
                