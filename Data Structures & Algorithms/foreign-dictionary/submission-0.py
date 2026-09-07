class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = {}

        for word in words:
            for c in word:
                if not c in chars:
                    chars[c] = set()

        #build the adjacency list

        for w in range(len(words)-1):

            w1 = words[w]
            w2 = words[w+1]

            for i in range(len(w1)):

                if len(w1) > len(w2) and w1[:len(w2)] == w2[:len(w2)]:
                    return ""
                if i < len(w2) and w1[i] != w2[i]:
                    chars[w1[i]].add(w2[i])
                    break 



        visited = set()

        res = []
        def dfs(node, curr):

            if node in curr:
                return True
            if node in visited:
                return False
            curr.add(node)

            for i in chars[node]:
                if dfs(i, curr):
                    return True 
            
            visited.add(node)
            curr.remove(node)
            res.append(node)
            return False
        for i in chars.keys():

            if dfs(i, set()):
                return ""

        return "".join(res[::-1])

                

            

        




        


        