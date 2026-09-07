class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        


        lst1 = [0]*26


        for i in range(len(s1)):


            lst1[ord(s1[i])-ord("a")] +=1


        slow = 0

        lst2 = [0]*26
        

        for i in range(len(s2)):


            if i >= len(s1):

                lst2[ord(s2[slow])-ord("a")] -=1

                slow +=1

            lst2[ord(s2[i])-ord("a")] +=1


            if lst2 == lst1:

                return True


        return False

                





