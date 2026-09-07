class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        

        left = 1

        right = max(piles)

        max_rate = right


        while left <= right:



            mid = (left+right)//2

            time = 0 


            for i in piles:

                time += (i + mid - 1) // mid
            

            if time > h:

                left = mid +1

            else:
                max_rate = min(max_rate, mid)

                right = mid-1

            

        return max_rate




