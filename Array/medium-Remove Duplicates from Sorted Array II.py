# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def removeDuplicates(self, nums):
        #nums: List[int]) -> int:
        i,j=0,2
        while j<len(nums):
            if nums[i]==nums[j]:
                del(nums[i])
            else:
                i+=1
                j+=1
        return len(nums)
        