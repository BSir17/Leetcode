# -*- coding:utf-8 -*-
# Code by Fan.Bai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        self.res=[]
        self.visit(root)
        return self.res

    def visit(self,root):
        if not root:
            return
        self.visit(root.left)
        self.res.append(root.val)
        self.visit(root.right)


class Solution:
    def inorderTraversal(self, root: TreeNode):
        mystack=[]
        cur=root
        res=[]
        while(cur or len(mystack)>0):
            if cur:
                mystack.append(cur)
                cur=cur.left
            else:
                cur=mystack.pop(-1)
                res.append(cur.val)
                cur=cur.right
        return res


    def pre(self,root):
        s=[]
        res=[]
        cur=root
        while (cur or len(s)>0):
            if cur:
                res.append(cur.val)
                s.append(cur)
                cur=cur.left
            else:
                cur=s.pop(-1).right
        return res







a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)

a.left=b
b.left=c
c.right=d
a.right=e
print(Solution().pre(a))












