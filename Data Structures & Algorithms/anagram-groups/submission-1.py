class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        dic = {}




        for i in strs:


            lst = sorted(i)

            new = ''.join(lst)

            if new in dic:

                dic[new].append(i)

            else:

                dic[new] = [i]

        return list(dic.values())
        