class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        '''
I see a moving sliding window 
we start at the first index 
if value smaller than initial 

move this pointer 

else move fast pointer

        '''



        max_profit = 0




        slow = 0
        fast = slow+1

        stack = []


        while fast < len(prices):


            if prices[slow] < prices[fast]:

                max_profit = max(max_profit, prices[fast]-prices[slow])
                fast +=1

                

                
            else:

                slow+=1
                fast = slow+1

                

        return max_profit


                
        