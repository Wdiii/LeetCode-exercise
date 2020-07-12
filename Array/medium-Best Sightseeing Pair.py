# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxScoreSightseeingPair(self, A):
        #A: List[int]) -> int:
        tem=A[0]+0
        res=0
        for j in range(1,len(A)):
            res=max(tem+A[j]-j,res)
            tem=max(tem,A[j]+j)
        return res
