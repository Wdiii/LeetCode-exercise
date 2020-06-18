# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        #root: TreeNode) -> List[str]:
        if root==None:
            return []
        self.res=[]
        self.paths(root,str(root.val))
        return self.res
    def paths(self,node,v):
        if node.left==None and node.right==None:
            self.res.append(v)
        if node.left:
            self.paths(node.left,v+"->"+str(node.left.val))
        if node.right:
            self.paths(node.right,v+"->"+str(node.right.val))
        