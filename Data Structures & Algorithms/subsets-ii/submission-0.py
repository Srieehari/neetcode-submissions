class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subset = []
        res = []

        nums.sort()

        def helper(index):


            if index >= len(nums):

                res.append(subset.copy())


                return


            subset.append(nums[index])

            helper(index + 1)

            nex_index = index + 1

            while nex_index < len(nums) and nums[nex_index] == nums[index]:

                nex_index +=1

            

            subset.pop()

            helper(nex_index)

        helper(0)

        return res