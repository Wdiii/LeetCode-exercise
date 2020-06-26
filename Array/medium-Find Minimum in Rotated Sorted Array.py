# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findMin(self, nums):
        #nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[-1]:
                left=mid+1
            else:
                right=mid
    