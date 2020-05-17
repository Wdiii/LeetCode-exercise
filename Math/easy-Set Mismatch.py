# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findErrorNums(self, nums):
        #nums: List[int]) -> List[int]:
        a=list(range(1,len(nums)+1))
        miss=sum(set(a))-sum(set(nums))
        dup=sum(nums)-sum(set(nums))
        return[dup,miss]
              