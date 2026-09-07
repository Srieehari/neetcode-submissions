# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        curr = dummy
        node1, node2 = l1, l2
        remainder = 0

        while node1 or node2 or remainder:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            total = val1 + val2 + remainder
            curr.next = ListNode(total % 10)
            remainder = total // 10

            curr = curr.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

        return dummy.next