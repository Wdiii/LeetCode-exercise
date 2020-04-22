# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def validMountainArray(self, A):
        if len(A)<3:
            return False
        max_place=A.index(max(A))
        if max_place == 0 or max_place == len(A)-1:
            return False
        for i in range(max_place):
            if A[i]>=A[i+1]:
                return False
        for j in range(max_place,len(A)-1):
            if A[j]<=A[j+1]:
                return False
        return True