class Solution:
    def rob(self, nums: List[int]) -> int:
        


        def h(start, finish):


            house1 = 0 
            house2 = 0 

            for i in range(start, finish+1):


                

                newRob = max(nums[i]+ house1, house2)
                house1 = house2
                house2 = newRob

            return house2

        

        return max(nums[0],h(0,len(nums)-2), h(1, len(nums)-1))