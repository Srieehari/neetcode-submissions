# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        


        def helper(node, left, right):


            if node is None:

                return True


            if not(left < node.val < right):

                return False

            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float('-inf'), float('inf'))

            


        
                

            
        


