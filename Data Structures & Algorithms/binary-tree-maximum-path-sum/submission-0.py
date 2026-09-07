# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]


        def dfs(root):


            if root is None:
                return 0


            left_max = dfs(root.left)
            right_max = dfs(root.right)


            truel = max(left_max, 0)
            truer = max(right_max, 0)


            res[0] = max(res[0], root.val+ truel + truer)

            return root.val + max(truel, truer)

        dfs(root)

        return res[0]
        



        
        