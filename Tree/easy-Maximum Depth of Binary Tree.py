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
    def maxDepth(self, root):
        #root: TreeNode) -> int:
        if root==None:
            return 0
        left=self.maxDepth(root.left)+1
        right=self.maxDepth(root.right)+1
        return max(left,right)
    