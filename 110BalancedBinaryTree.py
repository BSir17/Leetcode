# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    def judge(self,root):
        if not root:
            return 0,True
        lh,lf=self.judge(root.left)
        rh,rf=self.judge(root.right)
        if lf and rf:
            if math.fabs(lh-rh)<2:
                return max([lh,rh])+1,True
        return max([lh,rh])+1,False

    def isBalanced(self, root: TreeNode) -> bool:
        rh,rf=self.judge(root)
        return rf




