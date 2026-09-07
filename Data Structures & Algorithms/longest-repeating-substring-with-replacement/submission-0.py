class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        '''


we need a window that goes from the left 

slow and a fast 

if the fast != slow letter then while count < k: we go in the while loop 

length is fast-slow+1


        '''

        count = {}

        max_freq = 0

        left = 0
        longest = 0


        for right in range(len(s)):


            char = s[right]

            count[char] = count.get(char, 0) +1

            max_freq = max(max_freq, count[char])



            while (right-left+1)-max_freq > k:


                count[s[left]] -=1

                left +=1

            longest = max(longest, right-left+1)


        return longest
            

            
            
                

