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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        else:
            root.save=root.left
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(root.save)
            return root