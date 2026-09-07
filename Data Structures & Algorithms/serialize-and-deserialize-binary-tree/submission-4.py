# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:

            return "[]"

        res = []
        q = deque([root])

        while q:

            node = q.popleft()

            

        
            if node:

                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

            else:
                res.append("null")

        while res and res[-1] == "null":
            res.pop()
        return "[" + ",".join(res) + "]" 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None
        vals = data[1:-1].split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            # left
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            # right
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


