# -*- coding:utf-8 -*-
# Code by Fan.Bai


#前序第一个为根节点，去中序里找这个值，这个值左边的建立为根节点的左子树，右边的建立为根节点的右子树
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder:list, inorder:list):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        root=preorder[0]
        rootindex=inorder.index(root)
        root=TreeNode(root)
        root.left=self.buildTree(preorder[1:rootindex+1],inorder[0:rootindex])
        root.right=self.buildTree(preorder[rootindex+1:],inorder[rootindex+1:])
        return root










