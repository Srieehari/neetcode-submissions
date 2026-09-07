class PrefixTree:

    def __init__(self):

        self.children = [None] *26

        self.end = False


        

    def insert(self, word: str) -> None:

        node = self


        for letter in word:

            index = ord(letter)- ord("a")

            if node.children[index] == None:

                new = PrefixTree()

                node.children[index] = new

            node = node.children[index]
        node.end = True



    def search(self, word: str) -> bool:


        node = self


        for letter in word:


            index = ord(letter)- ord("a")


            if node.children[index] == None:

                return False

            node = node.children[index]

        return node.end

        
        

    def startsWith(self, prefix: str) -> bool:

        node = self

        for letter in prefix:

            index = ord(letter) - ord("a")

            if node.children[index] == None:

                return False

            node = node.children[index]
        return True
        
        