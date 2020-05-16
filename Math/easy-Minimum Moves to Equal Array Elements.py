# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minMoves(self, nums):
        #nums: List[int]) -> int:
        m=min(nums)
        count=0
        for ele in nums:
            count+=ele-m
        return count