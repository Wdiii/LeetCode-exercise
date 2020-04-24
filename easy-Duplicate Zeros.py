# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def duplicateZeros(self, arr):
        #arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr):
            if arr[i]==0:
                arr.insert(i+1,0) #list.insert(index, obj)
                arr.pop() #list.pop([index=-1])
                i+=1
            i+=1