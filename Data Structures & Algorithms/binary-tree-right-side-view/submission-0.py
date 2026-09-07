# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = deque()


        q.append(root)

        res = []



        while q:


            len_level = len(q)



            for i in range(len_level):

                node = q.popleft()


                if node.left:

                    q.append(node.left)

                if node.right:

                    q.append(node.right)

            res.append(node.val)
        return res



        