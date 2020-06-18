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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count=0
        if root==None:
            return count
        count+=self.findPath(root,sum)
        count+=self.pathSum(root.left,sum)
        count+=self.pathSum(root.right,sum)
        return count       
    def findPath(self,root,sum):
        res=0
        if root==None:
            return 0
        elif root.val==sum:
            res=1
        res+=self.findPath(root.left,sum-root.val) 
        res+=self.findPath(root.right,sum-root.val)
        return res    
        