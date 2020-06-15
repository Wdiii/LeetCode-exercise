# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def fourSum(self, nums, target):
        #nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        i=0
        while i<n-3:
            j=i+1
            while j<n-2:
                k,l=j+1,n-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]<target:
                        k+=1
                    else:
                        l-=1
                j+=1
                while j<n-2 and nums[j]==nums[j-1]:
                    j+=1
            i+=1
            while i<n-1 and nums[i]==nums[i-1]:
                i+=1
        return res
    