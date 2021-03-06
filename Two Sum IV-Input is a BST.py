#Runtime: 68 ms, faster than 97.02% of Python3 online submissions for Two Sum IV - Input is a BST.
#Memory Usage: 18.5 MB, less than 42.38% of Python3 online submissions for Two Sum IV - Input is a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        a=set()
        def h(node):
            if not node:
                return False
            if(k-node.val in a):
                return True
            a.add(node.val)
            return h(node.right) or h(node.left)
        return h(root)
