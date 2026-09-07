class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        '''

        we need a variable to find minimum eating rate
        it does not say we have to access the pile in order

        '''

    
        low = 1

        high = max(piles)

        min_eating = high



        

        


        while low <= high:


            mid = (low+high)//2

            rate = 0 


            for pile in piles:


                rate += math.ceil(pile/mid)

            if rate <= h:

                min_eating = min(min_eating, mid)

                high=  mid-1


            else:

                low = mid+1

        return min_eating




            






           









