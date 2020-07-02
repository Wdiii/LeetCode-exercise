# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        #nums: List[int], k: int) -> int:
        product,previous,res=1,0,0
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k and previous<=i:
                product//=nums[previous]
                previous+=1
            res+=i-(previous-1)
        return res
        