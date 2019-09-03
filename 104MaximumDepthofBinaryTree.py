# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)
        return max([lh,rh])+1




























