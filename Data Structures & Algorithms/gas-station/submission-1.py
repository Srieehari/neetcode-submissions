class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        


        cur_gas = 0 
        start = 0 
        total_gas = 0
        for i in range(len(gas)):


            cur_gas += gas[i]-cost[i]

            total_gas += gas[i]-cost[i]


            if cur_gas < 0:

                cur_gas = 0 

                start = i + 1




        if total_gas >= 0 :

            return start

        else:
            return -1

            





