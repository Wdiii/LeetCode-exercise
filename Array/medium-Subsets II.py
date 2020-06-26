# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def subsetsWithDup(self, nums):
        #nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for n in nums:
            for r in res[:]:
                x=r[:]
                x.append(n)
                if x not in res:
                    res.append(x)
        return res