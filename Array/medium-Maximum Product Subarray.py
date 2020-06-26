# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxProduct(self, nums):
        #nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        res=max(nums)
        tem=1
        for i in nums:
            if i!=0:
                tem*=i
                res=max(res,tem)
            else:
                tem=1
        tem=1
        for j in nums[::-1]:
            if j!=0:
                tem*=j
                res=max(res,tem)
            else:
                tem=1
        return res
