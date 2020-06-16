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
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        elif abs(self.countDepth(root.left)-self.countDepth(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    def countDepth(self,root):
        if root==None:
            return 0
        left=self.countDepth(root.left)+1
        right=self.countDepth(root.right)+1
        return max(left,right)