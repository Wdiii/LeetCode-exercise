# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findDuplicate(self, nums):
        # nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)!=1:
                return i
     
class Solution2:
    def findDuplicate(self, nums):
        return (sum(nums)-sum(set(nums)))/(len(nums)-len(set(nums)))