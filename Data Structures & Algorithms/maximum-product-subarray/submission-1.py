class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        curMin, curMax = 1, 1

        #base case

        res = max(nums)

        for i in nums:



            if i == 0:
                curMin,curMax = 1,1

            temp = curMax * i
            curMax = max(curMin*i, curMax*i, i)
            curMin = min(curMin*i, temp, i)

            res = max(res, curMax)

        return res


            