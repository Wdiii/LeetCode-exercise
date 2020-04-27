# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def decompressRLElist(self, nums):
        #nums: List[int]) -> List[int]:
        lst=[]
        i=0
        while i < len(nums)-1:
            a=nums[i]
            b=nums[i+1]
            lst.extend([b]*a)
            i+=2
        return lst