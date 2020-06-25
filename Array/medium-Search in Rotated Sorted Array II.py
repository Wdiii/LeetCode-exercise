# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def search(self, nums, target):
        #nums: List[int], target: int) -> bool:
        if not nums:
            return False
        num=list(set(nums))
        left,right=0,len(num)-1
        while left<=right:
            mid=(left+right)//2
            if num[mid]==target:
                return True
            elif num[left]<=num[mid]:
                if num[left]<=target<num[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if num[mid]<target<=num[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
        