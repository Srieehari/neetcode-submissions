class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        count_map = {}

        for i, letter in enumerate(s):


            count_map[letter] = i




        start = 0
        end = 0 

        res = []
        for i, letter in enumerate(s):

            end = max(end, count_map[letter])


            if end == i:

                res.append(end-start+1)


                start = i +1 




        return res










            




