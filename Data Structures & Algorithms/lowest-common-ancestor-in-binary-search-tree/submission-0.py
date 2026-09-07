# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        


        def find(node, val1, val2):

            if val1.val <= node.val <= val2.val or val2.val <= node.val <= val1.val:

                return node


            if node.val > val1.val and node.val > val2.val:

                return find(node.left, val1, val2)

            if node.val < val1.val and node.val < val2.val:

                return find(node.right, val1, val2)


            


        return find(root, p, q)




