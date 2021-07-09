# Runtime: 36 ms, faster than 99.47% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 17.1 MB, less than 5.76% of Python3 online submissions for Construct String from Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans=[]
        def h(node):
            if(node is None):
                return ans
            ans.append(str(node.val))
            if(node.left is None and node.right is not None):
                ans.append('()')
            if(node.left):
                ans.append('(')
                h(node.left)
                ans.append(')')
            if(node.right):
                ans.append('(')
                h(node.right)
                ans.append(')')
            return ans
        h(root)
        return "".join(ans)
