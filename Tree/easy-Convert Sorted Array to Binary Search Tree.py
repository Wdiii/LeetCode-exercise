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
    def sortedArrayToBST(self, nums):
        #nums: List[int]) -> TreeNode:
        return self.createNode(nums,0,len(nums)-1)
    def createNode(self,nums,l,r):
        if l>r:
            return None
        mid=(l+r)//2
        root=TreeNode(nums[mid])
        root.left=self.createNode(nums,l,mid-1)
        root.right=self.createNode(nums,mid+1,r)
        return root
    