class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new = set(nums)

        longest = 0

        for i in new:



            length = 1
            current = i
            while current +1 in new:

                current+=1
                length +=1

            longest = max(length, longest)


        return longest
            
            


        return count



            






            
        