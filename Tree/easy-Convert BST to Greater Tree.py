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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.sum=0 #用一个变量sum记录下需要加的值
        def convert(root):
            if not root:
                return
            convert(root.right)
            self.sum+=root.val
            root.val=self.sum
            convert(root.left)
        convert(root)
        return root
#BST的右子树都比该节点大，所以修改次序是右–>中–>左。
