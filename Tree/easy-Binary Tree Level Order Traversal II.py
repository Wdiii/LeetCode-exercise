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
    def levelOrderBottom(self, root):
        #root: TreeNode) -> List[List[int]]:
        res=[]
        parents=[root] if root!=None else []
        while parents:
            children=[]
            for p in parents:
                if p.left:
                    children.append(p.left)
                if p.right:
                    children.append(p.right)
            res.insert(0,[n.val for n in parents])
            parents=children
        return res
    