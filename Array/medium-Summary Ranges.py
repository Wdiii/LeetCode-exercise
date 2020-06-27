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
    
#another solution from leetcode
class Solution2:
    def summaryRanges(self, nums):
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        return res
