class Node:


    def __init__(self, val, key ):

        self.key = key


        self.val = val

        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):


        self.left = Node(0,0)

        self.right = Node(0,0)

        self.mapping = {}
        self.space = capacity

        self.left.next = self.right
        self.right.prev = self.left
        


    def remove(self, n):

        temp_r = n.next
        temp_l = n.prev

        temp_r.prev = temp_l
        temp_l.next = temp_r


        n.next = None
        n.prev = None

    def add(self, n):

        temp_r = self.right
        temp_l = self.right.prev


        temp_l.next = n
        n.prev = temp_l

        temp_r.prev = n

        n.next = temp_r
        
    def get(self, key: int) -> int:

        if key in self.mapping:

            self.remove(self.mapping[key])
            self.add(self.mapping[key])

            return self.mapping[key].val



        else:
            return -1


        
    def put(self, key: int, value: int) -> None:

        if key in self.mapping:

            self.remove(self.mapping[key])



        self.mapping[key] = Node(value, key)

        self.add(self.mapping[key])

        if len(self.mapping) > self.space:

            nur = self.left.next

            self.remove(self.left.next)
            del self.mapping[nur.key]

        




        


            

        




        
