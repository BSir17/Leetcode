# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Solution1 failed because value in left tree must all be smaller than root.val
class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if root==None:
            return True
        if not root.left and not root.right:
            return True
        l=self.isValidBST(root.left)
        r=self.isValidBST(root.right)
        if l and r :
            if not root.right and root.left.val<root.val:
                return True
            if not root.left and root.right.val>root.val:
                return True
            if  root.left and root.right and root.left.val<root.val and root.right.val>root.val :
                return True
        return False

# 先进行中序遍历，然后看是否升序
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        res=[]
        cur=root
        s=[]
        while (cur or len(s)>0):
            if cur :
                s.append(cur)
                cur=cur.left
            else:
                cur=s.pop(-1)
                res.append(cur.val)
                cur=cur.right
        if len(res)==1:
            return True
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.minmin=-float('inf')
        return self.isValidBST1(root)
    def isValidBST1(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif(self.isValidBST1(root.left)):
            if self.minmin<root.val:
                self.minmin=root.val
                return self.isValidBST1(root.right)
            return False
        return False

a=TreeNode(1)
b=TreeNode(1)
a.right=b
print(Solution().isValidBST(a))







