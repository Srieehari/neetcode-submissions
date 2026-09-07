# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:



        dic = {val:index for index, val in enumerate(inorder)}





        self.preindex = 0




        def func(left, right):

            if left > right:

                return None



            node_val = preorder[self.preindex]

            node = TreeNode(node_val)


            self.preindex += 1


            curr_index = dic[node_val]


            node.left = func(left, curr_index-1)
            node.right = func(curr_index+1, right)

            return node


        return func(0, len(inorder)-1)



