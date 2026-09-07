class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        
        '''''

two while loops one for before and one for after 




        '''''

        lst = [1]*len(nums)

        prefix = 1


        for i in range(len(nums)):

            lst[i] = prefix

            prefix*= nums[i]



        post = 1


        for i in range(len(nums)-1, -1, -1):


            lst[i]*=post

            post*= nums[i]


        return lst
        


        

        







