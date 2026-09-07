class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}




        


        def dfs(curr):


            if curr == 0:

                return 0

            
            if curr < 0:

                return float('inf')

            if curr in dp:

                return dp[curr]

            min_count = float('inf')
            for i in coins:

                amt = dfs(curr-i)


                if amt != float('inf'):


                    min_count = min(min_count, 1+ amt)

            dp[curr] = min_count


            return dp[curr]

        res = dfs(amount)

        if res != float('inf'):
            return res

        else:

            return -1











        


            




        