# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def subarraySum(self, nums, k):
        #nums: List[int], k: int) -> int:
        dic={0:1} #if nums[0]==k
        tem,res=0,0
        for n in nums:
            tem+=n
            if tem-k in dic:
                res+=dic[tem-k]
            if tem in dic:
                dic[tem]+=1
            else:
                dic[tem]=1
        return res
            
    