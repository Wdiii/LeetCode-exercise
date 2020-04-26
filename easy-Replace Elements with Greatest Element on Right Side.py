# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def replaceElements(self, arr):
        #arr: List[int]) -> List[int]:
        lst=[]
        for i in range(1,len(arr)):
            lst.append(max(arr[i:]))
        lst.append(-1)
        return lst

#need to improve the running time
class Solution1:
    def replaceElements(self, arr):
        prev = arr[-1]
        for i in (range(len(arr)-1))[::-1]:
            tmp = arr[i]
            curr = max(arr[i+1:])
            arr[i] = max(curr, prev)
            prev = max(prev, tmp)
        arr[-1] = -1   
        return arr