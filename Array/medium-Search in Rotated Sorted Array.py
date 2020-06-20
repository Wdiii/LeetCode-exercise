# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def search(self, nums, target):
        #nums: List[int], target: int) -> int:
        if len(nums)==1 and target==nums[0]:
            return 0
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if right-left==1:
                if target==nums[left]:
                    return left
                elif target==nums[right]:
                    return right
                else:
                    return -1
            if target==nums[left]:
                return left
            if target==nums[right]:
                return right
            if target==nums[mid]:
                return mid
            if nums[left]<nums[mid]:
                if target<nums[mid] and target>nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
        