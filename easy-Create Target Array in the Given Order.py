# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def createTargetArray(self, nums, index):
        #nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i,j in enumerate(nums):
            target.insert(index[i],j)
        return target