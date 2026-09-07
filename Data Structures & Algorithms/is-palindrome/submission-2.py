class Solution:
    def isPalindrome(self, s: str) -> bool:
        



    
        short = 0

        other = len(s)-1


        while short < other:


            while short < other and not s[short].isalnum() :

                short +=1
            

            while  short < other and not s[other].isalnum():

                other-=1

            if s[short].lower() == s[other].lower():

                short+=1
                other-=1

            else:

                return False


        return True