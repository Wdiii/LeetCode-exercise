# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def productExceptSelf(self, nums):
        # nums: List[int]) -> List[int]:
        res=[1]
        tem=1
        for i in range(len(nums)-1):
            tem=tem*nums[i]
            res.append(tem)
        tem=1
        for j in range(len(nums)-2,-1,-1):
            tem=tem*nums[j+1]
            res[j]=res[j]*tem
        return res
    