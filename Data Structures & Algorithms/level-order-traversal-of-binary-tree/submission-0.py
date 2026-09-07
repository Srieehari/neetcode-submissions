# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:

            return []


        q = deque()

        q.append(root)

        result = []
        




        while q:


            level_length = len(q)

            val = []


            for i in range(level_length):



                node = q.popleft()

                val.append(node.val)


                if node.left:

                    q.append(node.left)

                if node.right:

                    q.append(node.right)

            result.append(val)


        return result








            
            
        