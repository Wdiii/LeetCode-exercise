# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # nums: List[int]) -> List[int]:
        lst=[]
        rank=sorted(nums)
        for i in range(len(nums)):
            lst.append(rank.index(nums[i]))
        return lst