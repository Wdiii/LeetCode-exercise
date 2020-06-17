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
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        p=[root]
        res=1
        while p:
            c=[]
            for i in p:
                if i.left==None and i.right==None:
                    return res
                    break
                if i.left:
                    c.append(i.left)
                if i.right:
                    c.append(i.right)
            p=c
            res+=1
           