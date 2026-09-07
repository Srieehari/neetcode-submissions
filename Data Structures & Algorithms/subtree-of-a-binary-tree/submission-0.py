# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        





        def func1(node1, node2):


            if node1 is None and node2 is None:

                return True

            if node1 is None or node2 is None:

                return False


            if node1.val != node2.val:

                return False

            return func1(node1.left, node2.left) and func1(node1.right, node2.right)

        def dfs(node):
            if node is None:
                return False
            if node.val == subRoot.val:
                if func1(node, subRoot):

                    return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)