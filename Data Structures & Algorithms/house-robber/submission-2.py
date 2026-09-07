class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)< 2:
            return nums[0]

        h1 = 0 
        h2 = 0
        

        for n in nums:


            new = max(h1 + n, h2)

            h1 = h2

            h2 = new

        return h2




            
