# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minIncrementForUnique(self, A):
        #A: List[int]) -> int:
        if not A:
            return 0
        count=0
        A.sort()
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                dif=A[i-1]-A[i]+1
                A[i]=A[i-1]+1
                count+=dif
        return count
        