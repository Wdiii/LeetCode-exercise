# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root): 
        #root: TreeNode) -> bool: 
        if root==None:
            return True
        return self.isMirrorTree(root.left,root.right)
    def isMirrorTree(self, left, right):
            if left==None and right==None:
                return True
            elif left==None and right!=None:
                return False
            elif left!=None and right==None:
                return False
            elif left.val!=right.val:
                return False
            else:
                return self.isMirrorTree(left.right,right.left) and self.isMirrorTree(left.left,right.right)
