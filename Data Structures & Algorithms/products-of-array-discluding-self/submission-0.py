class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        
        val = 0

        result =[]

        


        while val < len(nums):

            num = 1

            for i in range(len(nums)):

                    
                if val != i:

                    num*=nums[i]

                
            result.append(num)

            val+=1

        return result









            



        

        


    




