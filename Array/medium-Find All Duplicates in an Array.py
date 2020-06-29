# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findDuplicates(self, nums):
        #nums: List[int]) -> List[int]:
        res= []
        for i in nums:
            if nums[abs(i)-1]<0:
                res.append(abs(i))
            else:
                nums[abs(i)-1]=-nums[abs(i)-1]
        return res
#do it without extra space
