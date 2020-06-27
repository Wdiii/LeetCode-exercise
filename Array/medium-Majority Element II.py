# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def majorityElement(self, nums):
        #nums: List[int]) -> List[int]:
        res=[]
        for i in set(nums):
            if nums.count(i)>len(nums)/3:
                res.append(i)
        return res
        