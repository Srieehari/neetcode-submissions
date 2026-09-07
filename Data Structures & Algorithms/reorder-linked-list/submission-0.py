# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next


        previous = None
        curr = slow.next


        slow.next = None

        while curr:

            next_node = curr.next

            curr.next = previous

            previous = curr
            curr = next_node

        

        first = head

        second = previous


        while second:

            tmp1 = first.next
            tmp2 = second.next


            first.next = second
            second.next = tmp1


            first = tmp1
            second = tmp2



