# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def triangleNumber(self, nums):
        #nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        res=0
        for i in range(len(nums)-1,1,-1):
            left,right=0,i-1
            while left<right:
                if nums[right]+nums[left]>nums[i]:
                    res+=right-left
                    right-=1
                else:
                    left+=1
        return res
