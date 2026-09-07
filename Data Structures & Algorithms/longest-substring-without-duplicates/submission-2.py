class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0


        slow = 0
       


        longest = 0

        seen = set()
        


        for index, character in enumerate(s):
            while slow < len(s) and character in seen:

                seen.remove(s[slow])

                slow+=1

            seen.add(character)
            print(seen)
            longest = max(longest, len(seen))

        return longest



        

            




            



        