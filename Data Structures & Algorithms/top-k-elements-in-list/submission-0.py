class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        dic = {}


        for i in nums:


            if i in dic:

                dic[i]+=1

            else:

                dic[i] = 1


        new_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse = True))


        
        result = []
        for i, key in enumerate(new_dic):
            if i == k:
                break
            result.append(key)

        return result



        