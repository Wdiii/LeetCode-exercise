# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        #s: int, nums: List[int]) -> int:
        l,r=0,0
        res=len(nums)+1
        tem=0
        while r<len(nums):
            tem+=nums[r]
            while tem>=s:
                res=min(res,r-l+1)
                tem-=nums[l]
                l+=1
            r+=1
        if res==len(nums)+1:
            return 0
        else:
            return res
        