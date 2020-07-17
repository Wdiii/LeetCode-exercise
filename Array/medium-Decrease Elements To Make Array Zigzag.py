# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def movesToMakeZigzag(self, nums):
        #nums: List[int]) -> int:
        ori=nums[:]
        count=0
        for i in range(1,len(nums),2):
            if i!=len(nums)-1:
                if nums[i]>=nums[i-1] or nums[i]>=nums[i+1]:
                    nums[i]=(min(nums[i-1],nums[i+1])-1)
            else:
                if nums[i]>=nums[i-1]:
                    nums[i]=nums[i-1]-1
        count=sum(ori)-sum(nums)
        nums=ori[:]
        count1=0
        for i in range(0,len(nums),2):
            if i!=0 and i!=len(nums)-1:
                if nums[i]>=nums[i-1] or nums[i]>=nums[i+1]:
                    nums[i]=min(nums[i-1],nums[i+1])-1
            elif i==0:
                if nums[i]>=nums[i+1]:
                    nums[i]=nums[i+1]-1
            else:
                if nums[i]>=nums[i-1]:
                    nums[i]=nums[i-1]-1
        count1=sum(ori)-sum(nums)
        return min(count,count1)
    