# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 02:42:24 2020

@author: Di Wang
"""

class Solution:
    def sortColors(self, nums):
        #nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right=0,len(nums)-1
        i=0
        while i<=right:
            if nums[i]==0:
                nums[i],nums[left]=nums[left],nums[i]
                left+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[right]=nums[right],nums[i]
                right-=1
            else:
                i+=1