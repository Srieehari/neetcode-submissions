class Solution:
    def minWindow(self, s: str, t: str) -> str:
        


       
        freq = {}


        for i in t:


            freq[i] = freq.get(i, 0) +1


        
        freq_sec = {}

        count = len(freq)

        res_len = float("inf")


        need = 0 

        slow = 0 
        res = ""


        for fast in range(len(s)):


            char = s[fast]


            freq_sec[char] = freq_sec.get(char, 0 )+1


            if char in freq and freq_sec[char] == freq[char]:

                need +=1

            while need == count:


                if (fast-slow+1) < res_len:


                    res = s[slow:fast+1]

                    res_len = fast-slow+1

                left_char = s[slow]

                freq_sec[left_char] -= 1

                if left_char in freq and freq_sec[left_char] < freq[left_char]:

                    need-=1

                slow +=1

        return res


                


            



        