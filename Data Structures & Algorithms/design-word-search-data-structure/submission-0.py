class WordDictionary:

    def __init__(self):
        self.children = [None]*26
        self.end = False
        

    def addWord(self, word: str) -> None:

        node = self


        for i in word:


            index = ord(i)-ord("a")

            if node.children[index] == None:

                new = WordDictionary()

                node.children[index] = new

            node = node.children[index]

        node.end = True


        

    def search(self, word: str) -> bool:


        def dfs(j, node):


            for i in range(j, len(word)):



                character = word[i]

                if character == ".":


                    for let in node.children:


                        if let and dfs(i+1, let):

                            return True

                    return False

                else:


                    index = ord(character)-ord("a")


                    if node.children[index] is None:

                        return False

                    node = node.children[index]

            return node.end
        
        return dfs(0, self)


        
