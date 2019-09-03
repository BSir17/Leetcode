# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invert(self,root):
        if not root:
            return
        if not root.left and not root.right:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root


a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left=b
a.right=c
a=Solution().invertTree(a)
print("dfsdfs")














