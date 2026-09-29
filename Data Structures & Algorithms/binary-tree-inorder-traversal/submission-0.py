# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res =[]

        def traverse(node):
            if node is None:
                return 
            traverse(node.left)
            self.res.append(node.val)
            traverse(node.right)
            return
        traverse(root)
        return self.res
        