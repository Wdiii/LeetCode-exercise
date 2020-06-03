# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minMoves2(self, nums):
        #nums: List[int]) -> int:
        m=len(nums)//2
        nums.sort()
        count=0
        for i in nums:
            count+=abs(i-nums[m])
        return count