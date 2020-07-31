# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        #arr: List[int], k: int, threshold: int) -> int:
        res=0
        target=k*threshold
        subset=sum(arr[0:k])
        for i in range(0,len(arr)-k+1):
            if i:
                subset=subset-arr[i-1]+arr[i+k-1]
            if subset>=target:
                res+=1
        return res
