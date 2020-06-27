# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def summaryRanges(self, nums):
        #nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        res=[]
        if len(nums)==1:
            res.append(str(nums[0]))
        i,j=0,1
        count=0
        while j<len(nums):
            if nums[i]+(j-i)==nums[j]:
                count+=1
                if j==len(nums)-1:
                    res.append(str(nums[i])+"->"+str(nums[j]))
                j+=1
            else:
                if count!=0:
                    res.append(str(nums[i])+"->"+str(nums[j-1]))
                    i=j
                else:
                    res.append(str(nums[i]))
                    i+=1
                if j==len(nums)-1:
                    res.append(str(nums[j]))
                j=i+1
                count=0
        return res
