# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxChunksToSorted(self, arr):
        #arr: List[int]) -> int:
        res,tem=0,0
        lst=sorted(arr)
        for i in range(len(arr)):
            tem=max(tem,arr[i])
            if lst[i]==tem:
                res+=1
                tem=0
        return res
  