# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findShortestSubArray(self, nums):
        #nums: List[int]) -> int:  
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        length=max(dic.values())
        lst=[]
        for k,v in dic.items():
            if v==length:
                lst.append(k)
        res=50000
        for j in lst:
            x=(len(nums)-nums[::-1].index(j))-nums.index(j)
            res=min(res,x)
        return res
        