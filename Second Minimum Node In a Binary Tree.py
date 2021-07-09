#Runtime: 24 ms, faster than 94.75% of Python3 online submissions for Second Minimum Node In a Binary Tree.
# Memory Usage: 14.1 MB, less than 75.26% of Python3 online submissions for Second Minimum Node In a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        m1,m2=inf,inf
        def h(node):
            nonlocal m1,m2
            if not node:
                return 
            m1=m1 if m1<node.val else node.val
            if(m1!=node.val):
                m2=m2 if m2<node.val else node.val
            if(node.left):
                h(node.left)
            if(node.right):
                h(node.right)
            return m2 if m2!=inf else -1
        return h(root)
