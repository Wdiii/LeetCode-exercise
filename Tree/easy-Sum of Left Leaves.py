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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None: 
            return 0
        count=0
        if root.left and root.left.left==None and root.left.right==None:
            count+=root.left.val
        return count+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        
        