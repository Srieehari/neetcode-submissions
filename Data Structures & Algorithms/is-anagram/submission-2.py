class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        

        if len(s) != len(t):

            return False


        lst = [0]*26


        for i in range(len(s)):

            lst[ord(t[i])-ord("a")] +=1
            lst[ord(s[i])-ord("a")] -=1

        for i in lst:

            if i != 0:
                return False
            
        return True
            

        

        
                