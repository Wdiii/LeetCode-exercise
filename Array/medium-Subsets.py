# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def subsets(self, nums):
        #nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x=temp[:]
                x.append(num)
                res.append(x)
        return res
    