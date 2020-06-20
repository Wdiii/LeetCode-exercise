# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def nextPermutation(self, nums):
        #nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i==0:
            nums.sort()
        else:
            j=i-1
            while i<len(nums)-1 and nums[i+1]>nums[j]:
                i+=1
            nums[i],nums[j]=nums[j],nums[i]
            nums[j+1:]=sorted(nums[j+1:])
            