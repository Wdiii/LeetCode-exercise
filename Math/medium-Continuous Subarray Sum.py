# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def checkSubarraySum(self, nums, k):
        #nums: List[int], k: int) -> bool:
        dic={0:-1} #preset
        start=0
        for i in range(len(nums)):
            start+=nums[i]
            if k!=0:
                start=start%k
            if start in dic:
                if i-dic[start]>=2:
                    return True
            else:
                dic[start]=i
        return False