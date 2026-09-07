class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        


        low = 0

        high = len(numbers)-1


        while low < high:


            val = numbers[low]+ numbers[high]



            if val == target:

                return [low+1, high+1]

            if val > target:


                high-=1

            if val < target:

                low+=1

        return []