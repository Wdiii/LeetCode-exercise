# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res=[]
        def addroot(root):
            if root.val not in res:
                res.append(root.val)
            if root.left:
                addroot(root.left)
            if root.right:
                addroot(root.right)
        addroot(root)
        res.sort()
        count=res[-1]
        for i in range(1,len(res)):
            count=min(count,res[i]-res[i-1])
        return count
    