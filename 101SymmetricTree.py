# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#分情况讨论，思路简洁明了
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.judge(root.left,root.right)

    def judge(self,l,r):
        if not l and not r:
            return True
        if not l and r:
            return False
        if not r and l:
            return False
        if l and r:
            return self.judge(l.left,r.right) and self.judge(l.right,r.left) and l.val==r.val

a=TreeNode(1)
b=TreeNode(0)
a.left=b
print(Solution().isSymmetric(a))