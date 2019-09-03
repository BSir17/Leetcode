# -*- coding:utf-8 -*-
# Code by Fan.Bai

#思路哦，maxv记录全局的最大路径和。nowmax记录的是从当前节点往下走能得到的最大值，pathmax即为经过当前节点能达到的路径
#最大值，肯定是左孩子路径最大和，右孩子最大路径和，当前节点的各种组合里最大的那个
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxv=-float("inf")
        self.maxpath(root)
        return self.maxv
    def maxpath(self,root):
        if not root:
            return 0
        lv=self.maxpath(root.left)
        rv=self.maxpath(root.right)
        nowmax=max([lv,rv])
        if nowmax>0:
            nowmax+=root.val
        else:
            nowmax=root.val
        pathmax=max([root.val,root.val+lv,root.val+rv,lv+root.val+rv])
        if pathmax>self.maxv:
            self.maxv=pathmax
        return nowmax











