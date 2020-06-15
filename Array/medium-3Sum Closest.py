# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def threeSumClosest(self, nums, target):
        #nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        res=sum(nums[:3])
        for i in range(n-2):
            j,k=i+1,n-1
            while j<k:
                tem=nums[i]+nums[j]+nums[k]
                if abs(target-tem)<abs(target-res):
                    res=tem
                if tem<target:
                    j+=1
                else:
                    k-=1
        return res
    