# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minStartValue(self, nums):
        #nums: List[int]) -> int:
        res=nums[0]
        for i in range(2,len(nums)+1):
            tem=sum(nums[:i])
            res=min(tem,res)
        if res>0:
            return 1
        else:
            return -res+1