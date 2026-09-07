# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        



        def find(node, max_val):



            if node is None:

                return 0


            if node.val >= max_val:

                return 1 + find(node.left, node.val) + find(node.right, node.val)

            else:

                return 0 + find(node.left, max_val) + find(node.right, max_val)

        return find(root, root.val)