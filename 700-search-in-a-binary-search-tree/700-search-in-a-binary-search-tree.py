# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return rec(root.right)
                return rec(root.left)

        return rec(root)
