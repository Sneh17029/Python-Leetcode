#Runtime: 188 ms, faster than 99.07% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 22.2 MB, less than 59.25% of Python3 online submissions for Range Sum of BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s=0
        def h(node):
            nonlocal s
            if not node:
                return
            if(low<=node.val<=high):
                s+=node.val
            if(node.val<low):
                return h(node.right)
            if(node.val>high):
                return h(node.left)
            h(node.left)
            h(node.right)
            return s
        return h(root)