#Runtime: 20 ms, faster than 99.48% of Python3 online submissions for Cousins in Binary Tree.
#Memory Usage: 14.4 MB, less than 8.18% of Python3 online submissions for Cousins in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def h(node,s,l):
            dl=0
            # print(node.val)
            nonlocal alp
            if not node:
                return 0
            if(node.val==s):
                return l,alp
            if(node.left):
                if(node.left.val==s):
                    alp=node.val
                dl,r=h(node.left,s,l+1)
            if(dl!=0 and alp!=0):
                return dl,alp
            if(node.right):
                if(node.right.val==s):
                    alp=node.val
                dl,r=h(node.right,s,l+1)
            return dl,alp
        alp=0
        g,a=h(root,x,0)
        alp=0
        f,b=h(root,y,0)
        print(g,a,f,b)
        return g==f and a!=b