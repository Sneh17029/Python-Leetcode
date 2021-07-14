#Runtime: 24 ms, faster than 96.57% of Python3 online submissions for Univalued Binary Tree.
#Memory Usage: 14.3 MB, less than 47.43% of Python3 online submissions for Univalued Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        a=root.val
        g=0
        def h(node):
            nonlocal g
            if not node:
                return
            if(g==1):
                return False
            if(node.val!=a):
                g=1
            if node.left:
                h(node.left)
            if node.right:
                h(node.right)
            return True if g==0 else False
        return h(root)