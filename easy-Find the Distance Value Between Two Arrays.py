# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        #arr1: List[int], arr2: List[int], d: int) -> int:
        count = len(arr1)
        for i in arr1:
            for j in list(set(arr2)):
                if abs(i-j) <= d:
                    count-=1
                    break
        return count