from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        chars = [set()for i in range(len(endWord))]
        for i in wordList:
            for s in range(len(i)):
                chars[s].add(i[s])

        words = set(wordList)

        if not endWord in words:
            return 0 

        q = deque()
        visited = set()
        q.append((beginWord, 1))
        visited.add(beginWord)


        while q:

            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):

                for c in chars[i]:

                    new = word[:i] + c + word[i+1:]

                    if new in words and not new in visited:
                        visited.add(new)
                        q.append((new, steps+1))

        return 0 

            

                        




        

       



        