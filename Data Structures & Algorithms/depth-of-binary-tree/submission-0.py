# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        




        def max_find(node):




            if node is None:

                return 0


            left = max_find(node.left) + 1

            right = max_find(node.right) + 1


            return max(left, right)

        return max_find(root)
