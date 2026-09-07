# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        

        


        ptr = head
        count = 0
        while ptr:

            count +=1

            ptr = ptr.next


        start = head
        prev = None

        if count == n:
            return head.next

        for _ in range((count-n)):

            
            prev = start

            start = start.next

        

        prev.next = start.next

        return head





        
