class Solution:
    def climbStairs(self, n: int) -> int:



        fib1 = 1
        fib2 = 1

        for i in range(n-1):

            fib1, fib2 = fib2, fib1+fib2

        return fib2

        
        

        
        




            