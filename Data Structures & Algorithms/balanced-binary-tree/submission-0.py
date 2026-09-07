# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        


        def helper(node):


            if node is None:

                return (0, True)


            left_len, left_bool = helper(node.left)

            right_len, right_bool = helper(node.right)


            current_balanced = (
    left_bool and
    right_bool and
    abs(left_len - right_len) <= 1
)



            return (1+max(left_len, right_len), current_balanced)


        lenght, boolean = helper(root)

        return boolean
            