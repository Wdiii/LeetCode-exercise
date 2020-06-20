# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def search(self, nums, target):
        #nums: List[int], target: int) -> int:
        if nums==[]:
            return [-1,-1]
        if target<=nums[-1] and target>=nums[0]:
            left,right=0,len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if target==nums[mid]:
                    left=mid
                    right=mid
                    while left>0 and nums[left]==nums[left-1]:
                        left-=1
                    while right<len(nums)-1 and nums[right]==nums[right+1]:
                        right+=1
                    return [left,right]
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return [-1,-1]
               