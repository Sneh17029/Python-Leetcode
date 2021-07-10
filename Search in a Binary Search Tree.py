# Runtime: 64 ms, faster than 97.44% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.1 MB, less than 65.74% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        n=TreeNode()    
        def h(node):
            nonlocal val
            nonlocal n
            if not node:
                return
            if node.val==val:
                n=node
                return n
            if(node.val>val):
                return h(node.left)
            if(node.val<val):
                return h(node.right)
            return None
        return h(root)
