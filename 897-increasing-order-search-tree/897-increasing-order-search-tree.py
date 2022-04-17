# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        temp = x = root
        i = 0
        while stack or temp:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                node = stack.pop()
                if i==0:
                    root = x = node
                    i+=1
                else:
                    x.right = node
                    x = node
                    x.left = None
                temp = node.right
        return root	