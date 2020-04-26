# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findSpecialInteger(self, arr):
        #arr: List[int]) -> int:
        if len(arr)<=3:
            return arr[0]
        else:
            n=len(arr)//4
            if arr.count(arr[n-1])>n:
                return arr[n-1]
            elif arr.count(arr[2*n-1])>n:
                return arr[2*n-1]
            else:
                return arr[3*n-1]