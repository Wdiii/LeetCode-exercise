# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isIdealPermutation(self, A):
        #A: List[int]) -> bool:
        #max(A[:i])<A[i+2]
        tem=0
        for i in range(len(A)-2):
            tem=max(A[i],tem)
            if tem>A[i+2]:
                return False
        return True