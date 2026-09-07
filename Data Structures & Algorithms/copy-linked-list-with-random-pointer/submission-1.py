"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        


        ptr = head

        dic ={}

        
        while ptr:

            dic[ptr] = Node(ptr.val)

            ptr= ptr.next


        new = head


        while new:


            if new.next:

                dic[new].next = dic[new.next]

            if new.random:



                dic[new].random = dic[new.random]

            new = new.next


        return dic[head]

            

        


        

        


            

            


        










            






            


