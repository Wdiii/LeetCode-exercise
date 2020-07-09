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
    def findMode(self, root):
        #root: TreeNode) -> List[int]:
        res=[]
        dic={}
        if root==None:
            return res
        def count(root):
            if root.val in dic:
                dic[root.val]+=1
            else:
                dic[root.val]=1
            if root.left:
                count(root.left)
            if root.right:
                count(root.right)
        count(root)
        mode=max(dic.values())
        for k,v in dic.items():
            if v==mode:
                res.append(k)
        return res
