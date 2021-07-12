#Runtime: 20 ms, faster than 99.78% of Python3 online submissions for Leaf-Similar Trees.
#Memory Usage: 14.4 MB, less than 40.34% of Python3 online submissions for Leaf-Similar Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def h(n1,l1):
            if not n1:
                return 
            if not n1.left and not n1.right and n1.val not in l1:
                l1.append(n1.val)
            if(n1.left):
                h(n1.left,l1)
            if(n1.right):
                h(n1.right,l1)
            return l1
        l1=[]
        l2=[]
        return (h(root1,l1))==(h(root2,l2))